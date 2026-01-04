# TIP Manila AI Chatbot Assistant

The **TIP Manila Chatbot** is an AI-powered automated solution designed to assist prospective students, parents, and alumni. It provides 24/7 instant responses to frequently asked questions (FAQs) regarding undergraduate programs, admissions, and institutional information.

## 📌 Table of Contents

* [I. Executive Summary](#i-executive-summary)
* [II. Introduction](#ii-introduction)
* [III. Methodology & Tech Stack](#iii-methodology--tech-stack)
* [IV. System Architecture](#iv-system-architecture)
* [V. System Features](#v-system-features)
* [VI. Results and Discussion](#vi-results-and-discussion)
* [VII. Conclusion and Recommendations](#vii-conclusion-and-recommendations)
---

## I. Executive Summary

The TIP Manila chatbot project provides an interactive, automated solution for answering FAQs regarding undergraduate programs. Developed using the OpenAI API for advanced natural language processing and Visual Studio Code for script development, the chatbot is hosted on OnRender to ensure 24/7 availability for students and parents worldwide.
## II. Introduction

### Background

Founded in 1962, T.I.P. is a premier technical institution. As the school shifts focus from Senior High School to specialized undergraduate and graduate degrees, this chatbot ensures that the transition in information (such as the suspension of SHS in Manila) is communicated accurately to the public.

### Objectives

* **General:** Deploy a high-fidelity chatbot using **OpenAI's GPT models** to handle TIP Manila inquiries.
* **Specific:** Use **System Prompts** to ground the AI in official school data and prevent "hallucinations" (inaccurate info).

## III. Methodology & Tech Stack

### Project Development Environment

* **OpenAI API (GPT-4o-mini):** The core logic engine used for Natural Language Understanding (NLU).
* **Python/Node.js:** Backend scripts to handle API calls and session management.
* **Visual Studio Code:** Primary environment for coding the interface.
* **OnRender:** Deployment platform for the live web application.

### Data Gathering

The AI's knowledge base is derived from:

1. **Official TIP Website:** Admission requirements and course lists.
2. **Consultations:** Common pain points identified by faculty and registrar staff.

## IV. System Architecture

The chatbot follows a request-response cycle where user input is sent via the OpenAI API, processed against a "System Instructions" set, and returned as a formatted response.

## V. System Features

* **Academic Navigator:** Detailed lists of Engineering, Computing, and Business programs.
* **Admission Assistant:** Step-by-step guides for Freshmen and Transferees.
* **Legacy & Vision:** Accurate historical data on the school's founding and current leadership.
* **Formatting Engine:** Responses utilize Markdown (Bold, Lists) for high readability.

## VI. Results and Discussion

### Transitioning from Google AI Studio to OpenAI

* **Observation:** OpenAI provided more consistent formatting for bulleted lists compared to previous iterations.
* **Challenge:** Managing API tokens and costs.
* **Solution:** Implemented **System Messages** to keep responses concise, effectively lowering token consumption without losing information quality.

## VII. Conclusion and Recommendations

The migration to OpenAI has enhanced the chatbot's ability to handle complex, multi-part questions (e.g., "What are the requirements for transferees and when does the registrar open?").

**Future Recommendations:**

* **RAG (Retrieval-Augmented Generation):** Connect the OpenAI API to a vector database of the TIP Student Manual for even deeper accuracy.
* **Voice Integration:** Utilizing OpenAI's Whisper model for voice-to-text inquiries.

---

### 🛠️ Sample OpenAI System Prompt Used

```text
"You are a helpful assistant for TIP Manila. 
Answer only based on the provided school data. 
If asked about SHS, clarify that it is only offered in Quezon City, not Manila. 
Use bullet points for requirements."

```

**Developed by:** Francesca Togonon
**Powered by:** OpenAI GPT API
