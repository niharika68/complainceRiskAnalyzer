# How the Compliance Risk Analyzer Works

## What Does This App Do?

This app automatically checks if healthcare organizations following the **340B drug pricing program** are managing it correctly and identifies **red flags** or risk areas.

The app runs through a step-by-step process (called a **workflow**) to:
1. Get customer data
2. Look up risk definitions
3. Compare data against risk thresholds
4. Search for recent regulatory updates
5. Get latest HRSA guidance
6. Create a final compliance report

---

## The Workflow Steps (Nodes)

### 1. **Retrieve Customer Metrics**
- Fetches customer data from AWS Bedrock Knowledge Base (S3-backed)
- Gets numbers like:
  - How many negative ordering incidents
  - Match rate percentages
  - Referral capture rates
- Parses data from CSV format into structured data

### 2. **Retrieve Knowledge Base**
- Gets risk definitions from the knowledge base
- Pre-indexes 3 main risk areas:
  - **Negative Accumulation Risk** - Ordering too many drugs without patient needs
  - **Match Rate Risk** - Low matching between drugs ordered and patient eligibility
  - **Referral Capture Risk** - Not capturing enough patient referrals

### 3. **Evaluate Risks**
- Compares each metric against risk thresholds
- Determines if each metric is: **Low Risk**, **Medium Risk**, or **High Risk**
- Creates a summary for each customer showing their risk profile

### 4. **Search Regulatory Updates**
- Searches DuckDuckGo for recent 340B compliance news
- Looks for updates on:
  - New compliance requirements
  - Diversion control updates
  - Patient eligibility changes

### 5. **Retrieve HRSA Guidance**
- Searches for latest information from HRSA (Health Resources and Services Administration)
- Finds current 340B program guidance and updates
- Gets latest compliance requirements

### 6. **Generate Report**
- Uses AI (Claude) to create an executive summary
- Creates a readable compliance report showing:
  - Which customers have risks
  - What the specific risks are
  - Latest HRSA guidance
  - Risk details and thresholds

---

## About the Data

### ⚠️ Important Note About S3Data Files

The files in the **S3Data/** folder are **SAMPLE COPIES ONLY**:
- `customermetrics.md` - Contains sample customer metrics
- `RiskIndicator.md` - Contains sample risk definitions

These are **NOT** the real data. They are used for:
- Local testing and development
- Understanding data structure and format
- Reference during development

### 📍 Where the REAL Data Lives

The **actual production data** is stored in:
- **AWS S3 bucket** - Contains the real customer metrics and risk definitions
- **AWS Bedrock Knowledge Base** - Retrieves data from the S3 bucket

When the app runs, it connects to AWS Bedrock and pulls the latest real data from S3.

---

## Output

The app creates a compliance report with:
- **Executive Summary** - AI-generated overview of key risks
- **Customer Risk Analysis** - Details for each customer:
  - Number of high/medium/low risk issues
  - Specific metric values
  - Risk thresholds
  - Risk descriptions
- **HRSA 340B Program Guidance** - Latest updates from web search
- **Metadata** - When the report was generated

The report is saved to: `compliance_output/risk_report.txt`

---

## Risk Thresholds

| Metric | Low Risk | Medium Risk | High Risk |
|--------|----------|-------------|-----------|
| **Negative Accumulation Count** | 0–5 | 6–15 | >15 |
| **Match Rate %** | >85% | 70–85% | <70% |
| **Referral Capture Rate %** | >60% | 40–60% | <40% |

---

## Technology Stack

- **Python** - Programming language
- **AWS Bedrock** - AI and knowledge base retrieval
- **Model LLM** - amazon.nova-lite-v1. Generates executive summaries
- **LangGraph** - Orchestrates the multi-step workflow
- **Pydantic** - Provides strict type validation and automatic data validation (defines RiskEvaluation and CustomerRiskReport models)
- **DuckDuckGo API** - Searches for regulatory updates from duckduckGo
- **Poetry** - Dependency management

---

## Future Updates

- **FastAPI** - Build a REST API to send compliance reports and risk data to downstream systems. 
- Real-time alerts - Notify stakeholders when high-risk issues are detected
- Dashboard visualization - Create an interactive dashboard to view compliance status through tableau API



