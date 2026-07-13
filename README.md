# ReachIQ-video-rag-engine
Semantic Video Retrieval & Competitive Intelligence Engine powering ReachIQ AI.

Built by ### Noreen Akbar

### Purpose

This repository contains the standalone Video RAG engine responsible for:

Video ingestion
Whisper transcription
OCR extraction
Semantic chunking
Embedding generation
Vector search
Competitive Intelligence generation

This engine is integrated into the main ReachIQ AI project.

### Main Project

https://github.com/NoreenAkbar/ReachIQ-AI

### Architecture
Competitor Videos
        ↓
Whisper + OCR
        ↓
Chunking
        ↓
Embedding Generation
        ↓
Supabase pgvector
        ↓
Semantic Retrieval (RAG)
        ↓
Gemma 3 4B (AMD ROCm + vLLM)
        ↓
Competitive Intelligence Engine
        ↓
Executive Intelligence Report

### Features
Semantic Video Search
Transcript Chunking
pgvector Retrieval
Competitive Intelligence
Hook Analysis
CTA Analysis
Thumbnail Intelligence
Viewer Psychology Analysis
Strategic Reasoning
Content Gap Detection
Recommended Video Blueprint

### Core Modules
File	Purpose
ingest.py	Downloads, transcribes, and indexes videos
storage.py	Stores chunks, embeddings, and metadata
query.py	Semantic retrieval and intelligence extraction
competitive_engine.py	Generates executive competitive intelligence reports
llm_provider.py	AMD Gemma / Groq provider abstraction
AMD Deployment

### Successfully validated on:

AMD Developer Cloud
ROCm 7.2
vLLM
Google Gemma 3 4B

### Validation:

✅ Gemma loaded successfully
✅ ROCm execution verified
✅ OpenAI-compatible endpoint tested
✅ Competitive Intelligence generated on AMD compute

### Integration

This repository is used as the intelligence backend for:

ReachIQ AI

https://github.com/NoreenAkbar/ReachIQ-AI

The main project imports this engine to provide:

Pre-upload intelligence
Competitor analysis
Content strategy
Market intelligence
AI-powered recommendations
Status

✅ AMD Developer Hackathon ACT II

Integrated into ReachIQ AI.
