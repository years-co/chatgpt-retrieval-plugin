from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Source(str, Enum):
    email = "email"
    file = "file"
    chat = "chat"


class DocumentMetadata(BaseModel):
    source: Optional[Source] = None
    source_id: Optional[str] = None
    created_at: Optional[str] = None
    author: Optional[str] = None
    url: Optional[str] = None
    rank: Optional[str] = None
    title: Optional[str] = None
    pmid: Optional[str] = None
    search_engine: Optional[str] = None
    year: Optional[str] = None
    journal: Optional[str] = None
    research_article: Optional[str] = None
    clinical_article: Optional[str] = None
    number_of_citations_from_clinical_articles: Optional[str] = None
    human: Optional[str] = None
    animal: Optional[str] = None
    molecular_cellular: Optional[str] = None
    nih_percentile: Optional[str] = None
    number_of_citations: Optional[str] = None
    approximate_potential_to_translate: Optional[str] = None


class DocumentChunkMetadata(DocumentMetadata):
    document_id: Optional[str] = None


class DocumentChunk(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentChunkMetadata
    embedding: Optional[List[float]] = None


class DocumentChunkWithScore(DocumentChunk):
    score: float


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: Optional[DocumentMetadata] = None


class DocumentWithChunks(Document):
    chunks: List[DocumentChunk]


class DocumentMetadataFilter(BaseModel):
    document_id: Optional[str] = None
    source: Optional[Source] = None
    source_id: Optional[str] = None
    author: Optional[str] = None
    start_date: Optional[str] = None  # any date string format
    end_date: Optional[str] = None  # any date string format
    url: Optional[str] = None
    rank: Optional[str] = None
    title: Optional[str] = None
    pmid: Optional[str] = None
    search_engine: Optional[str] = None
    year: Optional[str] = None
    journal: Optional[str] = None
    research_article: Optional[str] = None
    clinical_article: Optional[str] = None
    number_of_citations_from_clinical_articles: Optional[str] = None
    human: Optional[str] = None
    animal: Optional[str] = None
    molecular_cellular: Optional[str] = None
    nih_percentile: Optional[str] = None
    number_of_citations: Optional[str] = None
    approximate_potential_to_translate: Optional[str] = None


class Query(BaseModel):
    query: str
    filter: Optional[DocumentMetadataFilter] = None
    top_k: Optional[int] = 3


class QueryWithEmbedding(Query):
    embedding: List[float]


class QueryResult(BaseModel):
    query: str
    results: List[DocumentChunkWithScore]
