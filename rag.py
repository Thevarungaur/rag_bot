import os
import faiss
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer

import scraper  # scraper.py file

# Scrape the NIET website to get the documents needed to generate the "knowledge-base"
scraper.scrape_website()

# Load DPR context encoder
ctx_encoder = DPRContextEncoder.from_pretrained(
    'facebook/dpr-ctx_encoder-single-nq-base')
ctx_tokenizer = DPRContextEncoderTokenizer.from_pretrained(
    'facebook/dpr-ctx_encoder-single-nq-base')


# Read documents from the scraped_pages folder
# docs = []
# scraped_pages_folder = os.path.join(os.path.dirname(__file__), 'scraped_pages')
# for filename in os.listdir(scraped_pages_folder):
#     if filename.endswith('.txt'):
#         with open(os.path.join(scraped_pages_folder, filename), 'r', encoding='utf-8') as file:
#             content = file.read()
#             chunk_size = 1024
#             for i in range(0, len(content), chunk_size):
#                 chunk = content[i:i + chunk_size]
#                 docs.append(chunk)

# Hard-coding for testing
docs = [
    "Hansraj College, founded on 26th July 1948 by the D.A.V. College Managing Committee, is one of the largest constituent colleges of the University of Delhi, established in memory of Maharshi Dayanand Saraswati and Mahatma Hansraj.",
    "The college offers undergraduate and postgraduate education in Science, Commerce, and Arts to over 5000 students, guided by highly qualified academicians, and is known for excellence in academics, sports, and extracurricular activities.",
    "Hansraj College has completed 77 years of higher education, producing scholars, bureaucrats, intellectuals, and sportspersons who contribute nationally and internationally.",
    "The college boasts impressive infrastructure, including a Central Library, Departmental Libraries, six Computer Laboratories, eighteen Science Laboratories, a modern auditorium, seminar rooms, and hostel facilities for over 200 students.",
    "The college provides excellent sports facilities such as a vast field, football and basketball courts, an indoor sports complex, and the only Electronic Shooting Range in the University of Delhi.",
    "Scholarships are offered to deserving students, and the serene, lush green campus creates an inspiring environment for holistic growth and learning.",
    "The B.Sc. (Honours) Computer Science and B.Sc. Program (CS)/B.Sc. Physical Science with Computer Science equip students with interdisciplinary skills, logical thinking, programming expertise, and preparation for postgraduate studies like M.Sc., M.C.A., and M.B.A., or placements in various sectors.",
    "Distinguished alumni of the Computer Science Department include Professor (Dr.) Mamta Sareen (Kirori Mal College, DU), Dr. Harmeet Kaur (Hansraj College, DU), Mr. Anuj Goel (Director, Macquarie), Mr. Kushal Chawal (Film Director, Amazon Prime), and Ms. Ayushi Chirania (Higher Education, IIM Calcutta), among others."
]

# Tokenize and encode documents
inputs = ctx_tokenizer(docs, return_tensors="pt",
                       padding=True, truncation=True)
doc_embeddings = ctx_encoder(**inputs).pooler_output.detach().cpu().numpy()


# Create FAISS index (a vector data structure that holds all our "knowledge" in a format understandable by the LLM)
index = faiss.IndexFlatIP(doc_embeddings.shape[1])
index.add(doc_embeddings)


# Save document references
doc_map = {i: doc for i, doc in enumerate(docs)}


def retrieve(query):
    # Tokenize the query
    query_inputs = ctx_tokenizer(
        query, return_tensors="pt", padding=True, truncation=True)

    # Encode the query
    query_embedding = ctx_encoder(
        **query_inputs).pooler_output.detach().cpu().numpy()

    # Search the FAISS index for the "knowledge" that most closely matches the query
    D, I = index.search(query_embedding, k=1)
    retrieved_doc = doc_map[I[0][0]]

    return retrieved_doc