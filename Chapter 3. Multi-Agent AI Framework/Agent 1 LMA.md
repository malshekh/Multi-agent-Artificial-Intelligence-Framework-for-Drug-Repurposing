# Creating a Literature Mining Agent (LMA)
---
## Answering the questions
**1. What problem will the agent solve?**
PubMed contains more than 39 million publications, and thousands of new articles are published every week. Information relevant to a single research question is usually scattered across multiple journals and databases. Researchers spend a huge chunk of their time performing repetitive literature searches, screening abstracts, extracting information and identifying connections between studies, and this challenge is especially pronounced in interdisciplinary fields. The literature mining agent addresses this problem by autonomously retrieving, filtering, organizing, analyzing, and summarizing scientific literature while identifiying biological relationships and potential research gaps.
> Problems the agent aims to reduce:
- Manual PubMed searches
- Time spent reading irrelevant papers
- Duplicate literature screening
- Inconsistent literature organization
- Missed publications
- Human bias during article selection
- Fragmented knowledge across disciplines
  
**2. Who will use it?**

 Personal Use.
 
**3. What outcomes should it achieve?**
- Automatically screen publications based on relevance, keywords, journal quality and publication date.
- Retrieve relevant scientific publications.
- Identify research gaps, that will support hypothesis generation.
- Identify biological relationships (that can later be passed to a Knowledge Graph Agent).
- Generate machine-readable data to allow downstream agents to perform further analysis.
  
**4. How will success be measured?**
- [ ] Retrieval Performance: Assess if the agent found the relevant papers via precision, recall and/or F1-score.
- [ ] Relevance Ranking: Assess if the most important papers are ranked highly via Mean Reciprocal Rank (MRR) and/or Normalized Discounted Cumulative Gain (NDCG).
- [ ] Literature Coverage: Assess if the agent retrieved the major landmark publications by measuring percentage of benchmark papers identified, coverage across databases and diversity of journals.
- [ ] Research Gap Detection
- [ ] Time Efficiency: Compare the time required for manural literature review vs agent-assisted literature review by measuring the hours saved and number of papers processed per hour.
- [ ] Reproducibility: Running the same query under the same conditions should procude consistent results and any differences should be explainable. 
