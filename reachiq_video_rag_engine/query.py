from reachiq_video_rag_engine.storage import supabase
from reachiq_video_rag_engine.llm_provider import ask_llm


def get_chunks_for_niche(niche, limit=50):
    videos = supabase.schema("video_rag").table("videos").select("id").eq("niche", niche).execute().data
    video_ids = [v["id"] for v in videos]
    if not video_ids:
        return []
    chunks = supabase.schema("video_rag").table("chunks").select("*").in_("video_id", video_ids).limit(limit).execute().data
    return chunks


def extract_viral_hooks(niche):
    chunks = get_chunks_for_niche(niche)
    hook_chunks = [c["chunk_text"] for c in chunks if c.get("start_time", 999) < 15]
    if not hook_chunks:
        return None

    prompt = f"""
Analyze these opening hooks (first 15 seconds) from top videos in the '{niche}' niche.
Identify common viral hook patterns.

Return ONLY valid JSON, no extra text.
FORMAT:
{{"common_patterns": [], "best_examples": [], "recommended_hook_style": ""}}

HOOKS:
{chr(10).join(hook_chunks[:20])}
"""
    return ask_llm(prompt)


def extract_cta_patterns(niche):
    chunks = get_chunks_for_niche(niche)
    end_chunks = [c["chunk_text"] for c in chunks if c.get("end_time", 0) > 0][-20:]
    if not end_chunks:
        return None

    prompt = f"""
Analyze these closing segments from top videos in the '{niche}' niche.
Identify common call-to-action (CTA) patterns.

Return ONLY valid JSON, no extra text.
FORMAT:
{{"common_cta_patterns": [], "best_examples": [], "recommended_cta_style": ""}}

SEGMENTS:
{chr(10).join(end_chunks)}
"""
    return ask_llm(prompt)


def analyze_pacing(niche):
    videos = supabase.schema("video_rag").table("videos").select("id").eq("niche", niche).execute().data
    video_ids = [v["id"] for v in videos]
    if not video_ids:
        return None

    scenes = supabase.schema("video_rag").table("scene_analysis").select("*").in_("video_id", video_ids).execute().data
    scene_counts = {}
    for s in scenes:
        scene_counts[s["video_id"]] = scene_counts.get(s["video_id"], 0) + 1

    prompt = f"""
Given these scene-cut counts per video in the '{niche}' niche, describe the pacing pattern
(cuts per minute, fast vs slow pacing trend).

Return ONLY valid JSON, no extra text.
FORMAT:
{{"average_cuts_per_video": 0, "pacing_style": "", "recommendation": ""}}

SCENE COUNTS: {list(scene_counts.values())}
"""
    return ask_llm(prompt)


def get_niche_intelligence(niche):
    """
    Single entry point combining all query functions.
    Used by Streamlit's final recommendation step.
    Returns None gracefully if no data indexed yet.
    """
    videos = supabase.schema("video_rag").table("videos").select("id").eq("niche", niche).execute().data
    if not videos:
        return None

    return {
        "viral_hooks": extract_viral_hooks(niche),
        "cta_patterns": extract_cta_patterns(niche),
        "pacing": analyze_pacing(niche)
    }