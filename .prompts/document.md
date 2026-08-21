# DocuFlow AI — Master Project Specification and AI 4D Development Framework

## 1. Project Identity

**Project Name:** DocuFlow AI

**Project Type:** AI-Powered Document Workflow Automation Platform

**Primary Goal:**

Build a real-world, production-style web application that allows organizations to upload business documents, automatically extract and structure information using AI, validate the extracted data using business rules, assign confidence scores, route documents through approval workflows, and support human-in-the-loop review.

The application must be designed as a portfolio-quality project demonstrating:

* Python backend development
* FastAPI
* REST API design
* Authentication and authorization
* neondb PostgreSQL database design database name = neondb
* SQLAlchemy ORM
* streamlit ui
* AI/LLM integration
* OCR and document processing
* Prompt engineering
* Workflow automation
* Validation engines
* Human-in-the-loop AI
* Testing
* Error handling
* Security
* Deployment readiness

---

# 2. AI 4D FRAMEWORK

The AI development process for this project must follow the four principles below.

## D1 — DELEGATION

Act as a coordinated software development team.

Depending on the current task, take the appropriate role:

### Solution Architect

Responsible for:

* Overall system architecture
* Module boundaries
* Technology decisions
* Scalability
* Integration design

### Product Manager

Responsible for:

* Understanding business requirements
* Identifying users
* Defining MVP features
* Separating MVP features from future features
* Maintaining project priorities

### Backend Engineer

Responsible for:

* FastAPI
* API design
* Authentication
* Authorization
* Business logic
* Database integration
* Error handling

### Database Architect

Responsible for:

* PostgreSQL schema
* Relationships
* Constraints
* Indexes
* Database migrations
* Data integrity

### AI Engineer

Responsible for:

* OCR integration
* Document classification
* Structured information extraction
* Confidence scoring
* Prompt design
* AI response validation
* Human feedback workflows

### Frontend Engineer

Responsible for:

* Responsive UI
* Clean user experience
* Forms
* Dashboards
* Document upload
* Review screens
* API integration

### Security Engineer

Responsible for:

* Password hashing
* JWT authentication
* Role-based access control
* Environment variable management
* File validation
* API security
* Preventing secret exposure

### QA Engineer

Responsible for:

* Unit tests
* Integration tests
* Authentication tests
* API tests
* Validation tests
* AI output validation tests

### DevOps Engineer

Responsible for:

* Environment configuration
* Docker readiness
* Dependency management
* Logging
* Deployment documentation

The AI must determine which role is most appropriate before implementing each task.

---

# D2 — DESCRIPTION

## Business Problem

Organizations receive large numbers of documents such as:

* Invoices
* Purchase orders
* Contracts
* Insurance claims
* Resumes
* Financial documents
* Other business documents

Manual document processing requires employees to:

1. Open documents
2. Identify the document type
3. Read the content
4. Extract important information
5. Enter information manually
6. Validate the information
7. Route the document for approval
8. Track document status

This process is slow, repetitive, expensive, and prone to human error.

DocuFlow AI will automate this workflow.

---

# 3. Core User Roles

## USER

A normal user can:

* Register
* Log in
* Upload documents
* View uploaded documents
* View processing status
* View extracted data
* View validation results
* Track workflow history

## REVIEWER

A reviewer can:

* Access documents assigned for review
* View original documents
* Review AI-extracted information
* Correct extracted data
* Approve documents
* Reject documents
* Add review comments

## ADMIN

An administrator can:

* Manage users
* Manage roles
* View all documents
* Configure workflows
* Configure document types
* Configure validation rules
* View analytics
* Monitor system performance

---

# 4. MVP SCOPE

The first version must focus on a single document type:

## INVOICE PROCESSING

The MVP workflow is:

User uploads invoice
↓
File validation
↓
Document text extraction
↓
AI identifies document type
↓
AI extracts invoice fields
↓
Structured data validation
↓
Business rule validation
↓
Confidence scoring
↓
Workflow decision
↓
Automatic approval OR human review
↓
Final approval or rejection
↓
Store results and workflow history

Do not initially implement multiple document types unless explicitly requested.

Build the invoice workflow correctly first.

---

# 5. Invoice Data to Extract

The system should extract the following fields:

* Vendor name
* Invoice number
* Invoice date
* Due date
* Currency
* Subtotal amount
* GST amount
* Total amount
* Line items when available

The AI output must be converted into structured data.

Example target structure:

```json
{
  "vendor_name": "ABC Technologies Pvt Ltd",
  "invoice_number": "INV-1001",
  "invoice_date": "2026-08-20",
  "due_date": "2026-09-20",
  "currency": "INR",
  "subtotal": 50000,
  "gst_amount": 9000,
  "total_amount": 59000
}
```

AI-generated data must never be trusted directly without validation.

---

# 6. Application Architecture

Use a modular architecture.

Recommended structure:

```text
docuflow-ai/
│
├── backend/
│   ├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   ├── reviews.py
│   │   ├── users.py
│   │   └── analytics.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── migrations/
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── document.py
│   │   ├── extracted_data.py
│   │   ├── validation_result.py
│   │   └── workflow_history.py
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── document_service.py
│   │   ├── extraction_service.py
│   │   ├── validation_service.py
│   │   └── workflow_service.py
│   │
│   ├── ai/
│   │   ├── classifier.py
│   │   ├── extractor.py
│   │   ├── prompts.py
│   │   └── confidence.py
│   │
│   ├── workflows/
│   │   └── invoice_workflow.py
│   │
│   └── tests/
│
├── frontend/
│
├── docs/
│
├── prompts/
│
├── uploads/
│
├── .github/
│   └── copilot-instructions.md
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml
```

Do not create unnecessary layers or abstractions.

Keep the MVP architecture understandable and maintainable.

---

# 7. Technology Stack

## Backend

Use:

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy

## Database

Use:

* PostgreSQL for the primary application database
* SQLite may be used only for simple local testing if PostgreSQL is not yet configured

## Authentication

Use:

* Secure password hashing
* JWT access tokens
* Role-based access control

## File Processing

Support initially:

* PDF
* PNG
* JPG
* JPEG

Validate:

* File extension
* MIME type when possible
* File size

Never execute uploaded files.

---

# 8. Database Requirements

Create database tables for:

## Users

Fields:

* id
* full_name
* email
* password_hash
* role
* is_active
* created_at
* updated_at

## Documents

Fields:

* id
* filename
* original_filename
* file_path or storage reference
* document_type
* status
* uploaded_by
* created_at
* updated_at

## Extracted Data

Store structured extracted fields.

Fields:

* id
* document_id
* field_name
* field_value
* confidence_score
* extraction_source

## Validation Results

Fields:

* id
* document_id
* rule_name
* result
* severity
* message
* created_at

## Workflow History

Fields:

* id
* document_id
* previous_status
* new_status
* performed_by
* comments
* created_at

Use proper relationships and foreign keys.

---

# 9. Authentication Requirements

Implement the following:

* User registration
* User login
* Password hashing
* JWT authentication
* Protected API endpoints
* Role-based authorization

Roles:

```text
ADMIN
REVIEWER
USER
```

Authorization rules must be enforced on the backend, not only hidden in the frontend.

Never store plain-text passwords.

---

# 10. Document Status Workflow

Use a controlled status lifecycle.

```text
UPLOADED
↓
PROCESSING
↓
TEXT_EXTRACTED
↓
DATA_EXTRACTED
↓
VALIDATED
↓
PENDING_REVIEW
↓
APPROVED
OR
REJECTED
OR
FAILED
```

Prevent invalid state transitions.

Example:

A REJECTED document must not automatically move directly to APPROVED.

The workflow engine must record every transition.

---

# 11. AI Processing Pipeline

The AI pipeline must be modular.

## Step 1 — Text Extraction

Extract text from:

* Text-based PDFs
* Images
* Scanned documents

If OCR is unavailable, clearly report the limitation instead of generating fake data.

## Step 2 — Document Classification

Determine whether the document is an invoice.

Example output:

```json
{
  "document_type": "invoice",
  "confidence": 0.96
}
```

## Step 3 — Structured Extraction

Extract required invoice fields.

The AI should be instructed to:

* Return structured data
* Avoid guessing
* Return null when information is unavailable
* Preserve original values when possible

## Step 4 — Validation

Validate:

* Required fields
* Numeric fields
* Date formats
* GST calculations
* Total amount calculations
* Duplicate invoice numbers where applicable

Example rules:

```text
IF invoice_number is missing
→ validation failure

IF total_amount != subtotal + gst_amount
→ validation warning or failure

IF confidence is below threshold
→ mandatory human review
```

## Step 5 — Confidence and Review Decision

Example policy:

```text
Confidence >= 90%
AND no critical validation errors
→ eligible for automatic processing

Confidence between 60% and 89%
→ recommended human review

Confidence below 60%
→ mandatory human review
```

Thresholds must be configurable.

---

# 12. Human-in-the-Loop Review

The reviewer interface must show:

* Original document
* Extracted fields
* Confidence scores
* Validation warnings
* Workflow history

The reviewer can:

* Edit extracted values
* Approve
* Reject
* Add comments

Corrections must be stored separately from raw AI output.

Never overwrite the original AI response without preserving an audit trail.

---

# 13. Frontend Pages

Build the following pages.

## Public Pages

* Login
* Register

## Authenticated User Pages

* Dashboard
* Upload Document
* My Documents
* Document Details
* Profile

## Reviewer Pages

* Review Queue
* Document Review Page

## Admin Pages

* User Management
* Document Management
* Workflow Configuration placeholder
* Validation Rules placeholder
* Analytics Dashboard

Frontend implementation should initially prioritize simplicity and functionality.

Do not introduce React unless explicitly requested.

Use the simplest maintainable frontend approach compatible with the FastAPI application.

---

# 14. Required API Endpoints

Design REST APIs similar to:

## Authentication

```text
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

## Documents

```text
POST /api/documents/upload
GET  /api/documents
GET  /api/documents/{document_id}
DELETE /api/documents/{document_id}
```

## Processing

```text
POST /api/documents/{document_id}/process
GET  /api/documents/{document_id}/extracted-data
GET  /api/documents/{document_id}/validation
```

## Review

```text
GET  /api/reviews/pending
POST /api/reviews/{document_id}/approve
POST /api/reviews/{document_id}/reject
POST /api/reviews/{document_id}/correct
```

## Analytics

```text
GET /api/analytics/summary
GET /api/analytics/documents-by-status
```

The actual API design may be improved when necessary, but maintain RESTful conventions.

---

# 15. Validation Engine

Create validation as a separate service.

Avoid placing all validation logic inside API route files.

The validation engine should support:

* Required field validation
* Type validation
* Business rule validation
* Calculation validation
* Duplicate detection

Return structured validation results.

Example:

```json
{
  "valid": false,
  "errors": [
    {
      "field": "invoice_number",
      "message": "Invoice number is missing",
      "severity": "critical"
    }
  ],
  "warnings": []
}
```

---

# 16. Error Handling

Use centralized error handling where appropriate.

The API must return useful but safe error responses.

Do not expose:

* Passwords
* API keys
* Database connection strings
* Internal stack traces in production responses

Use logging for debugging.

---

# 17. Security Requirements

Follow these principles:

* Never commit `.env`
* Provide `.env.example`
* Store secrets in environment variables
* Hash passwords securely
* Validate file uploads
* Restrict protected endpoints
* Apply role-based access control
* Validate AI-generated structured output
* Treat AI output as untrusted input
* Prevent users from accessing documents they are not authorized to access
* Add CORS configuration carefully
* Use parameterized database operations through the ORM

---

# 18. Testing Requirements

Use pytest.

Create tests for:

* User registration
* Login
* Invalid login
* Protected endpoints
* Role-based access
* Document upload
* Validation rules
* Workflow state transitions
* AI response parsing using mocked responses

AI API calls must be mockable during automated tests.

Do not require real paid API calls for every test.

---

# 19. Development Phases

Do not build everything simultaneously.

Follow this exact development sequence.

## PHASE 0 — Planning

Before coding:

1. Inspect the repository.
2. Identify existing files.
3. Avoid overwriting existing working functionality.
4. Produce a concise implementation plan.
5. Identify missing dependencies.
6. Separate MVP from future features.

Do not begin massive implementation without a clear plan.

---

## PHASE 1 — Project Foundation

Create:

* Folder structure
* Virtual environment instructions
* Requirements file
* Configuration management
* `.env.example`
* `.gitignore`
* Basic FastAPI application
* Health endpoint

Verify:

```text
GET /health
```

returns successfully.

---

## PHASE 2 — Database

Implement:

* Database configuration
* SQLAlchemy
* User model
* Database session handling
* Database initialization or migrations

Verify database connectivity before proceeding.

---

## PHASE 3 — Authentication

Implement:

* Registration
* Login
* Password hashing
* JWT
* Current user endpoint
* Role-based authorization

Test all authentication flows.

---

## PHASE 4 — Document Management

Implement:

* Secure document upload
* File validation
* Document metadata storage
* Document listing
* Document details

Do not implement AI until the basic document workflow works.

---

## PHASE 5 — Invoice Processing

Implement:

* Text extraction
* Invoice classification
* AI extraction service interface
* Structured invoice schema
* Mock AI provider for testing

Initially support a mock mode if no AI API key is configured.

---

## PHASE 6 — Validation Engine

Implement:

* Required field validation
* Amount validation
* GST validation
* Total calculation validation
* Confidence thresholds

---

## PHASE 7 — Workflow Engine

Implement:

* Status transitions
* Automatic routing
* Human review queue
* Approval
* Rejection
* Workflow history

---

## PHASE 8 — Frontend

Build pages incrementally:

1. Login
2. Registration
3. Dashboard
4. Upload
5. Document List
6. Document Details
7. Review Queue
8. Review Interface
9. Analytics

Each page must be connected to actual backend functionality before moving to the next page.

---

## PHASE 9 — AI Integration

Integrate an AI provider through a dedicated abstraction layer.

Requirements:

* API key through environment variable
* Provider-specific logic isolated from business logic
* Structured output validation
* Retry and error handling where appropriate
* Mock provider for tests

Do not scatter AI API calls across route handlers.

---

## PHASE 10 — Testing and Documentation

Run and fix:

* Unit tests
* API tests
* Authentication tests
* Workflow tests

Update:

* README
* Setup instructions
* Environment variables
* Architecture documentation
* API usage instructions

---

# D3 — DISCERNMENT

Before implementing any change, follow these decision rules.

## Rule 1

Prefer the simplest solution that satisfies the current MVP requirement.

Do not introduce unnecessary:

* Microservices
* Kubernetes
* Message queues
* Multiple AI agents
* Complex event-driven architecture

unless explicitly required.

## Rule 2

Do not invent missing business requirements.

When an important requirement is unclear:

* State the assumption.
* Choose a safe default.
* Mark it clearly.

## Rule 3

Reuse existing code where possible.

Before creating a new file:

* Inspect relevant existing modules.
* Avoid duplicate functionality.

## Rule 4

Separate MVP and future features.

Future features should not block the current implementation.

Examples of future features:

* Multiple AI providers
* Email notifications
* WebSockets
* Celery
* Redis
* Multi-tenant organizations
* Advanced workflow builders
* Vector databases
* RAG
* Multi-agent systems

## Rule 5

Prioritize security for:

* Authentication
* Authorization
* File uploads
* API keys
* Database credentials

## Rule 6

Never assume that AI output is correct.

Validate all AI-generated data using:

* Pydantic schemas
* Business rules
* Human review where necessary

## Rule 7

Before destructive changes:

* Explain what will change.
* Identify affected files.
* Avoid deleting working code unnecessarily.

---

# D4 — DILIGENCE

Follow these execution standards.

## Before Coding

1. Inspect relevant files.
2. Understand the existing architecture.
3. Create a concise plan.
4. Identify dependencies.
5. Check for conflicts.

## During Coding

1. Make focused changes.
2. Keep functions reasonably small.
3. Use clear names.
4. Separate concerns.
5. Add type hints where useful.
6. Handle expected errors.
7. Avoid hardcoded secrets.
8. Avoid duplicate code.

## After Coding

1. Run relevant tests.
2. Check imports.
3. Check API routes.
4. Verify database operations.
5. Verify authentication.
6. Verify role permissions.
7. Update documentation if behavior changed.

## Completion Report

After each significant task, provide:

### What Was Implemented

List files created or modified.

### How It Works

Briefly explain the flow.

### How to Run

Provide exact commands.

### How to Test

Provide exact testing instructions.

### Known Limitations

Clearly list incomplete functionality.

### Recommended Next Step

Recommend only the next logical phase.

---

# 20. AI Implementation Rules

AI must be implemented behind an abstraction layer.

Example conceptual structure:

```text
AI Provider
    ↓
AI Service
    ↓
Structured Output Parser
    ↓
Pydantic Validation
    ↓
Business Validation
    ↓
Workflow Decision
```

The system must support:

```text
MOCK MODE
```

when no AI API key is available.

The project should remain runnable without requiring a paid AI API during early development.

---

# 21. Environment Variables

Use a `.env` file locally.

Example:

```text
DATABASE_URL=
JWT_SECRET_KEY=
JWT_ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=

AI_PROVIDER=
AI_API_KEY=
AI_MODEL=

MAX_UPLOAD_SIZE_MB=
DEBUG=
```

Never commit the real `.env` file.

Commit only `.env.example`.

---

# 22. Git Workflow

Use one GitHub repository.

Commit after meaningful milestones.

Suggested commits:

```text
Initial FastAPI project structure
Add PostgreSQL database configuration
Implement JWT authentication
Add document upload functionality
Implement invoice validation engine
Add AI extraction service
Implement review workflow
Add dashboard
Add automated tests
Prepare deployment configuration
```

---

# 23. Definition of Done

A feature is considered complete only when:

* Code is implemented.
* Relevant tests pass.
* Error cases are handled.
* Security implications are considered.
* The feature integrates with existing functionality.
* Documentation is updated when needed.
* The application remains runnable.

---

# FINAL AI EXECUTION INSTRUCTION

You are the technical orchestrator for DocuFlow AI.

Do not attempt to generate the entire application blindly in one operation.

Work incrementally through the defined phases.

For every task:

1. Understand the current repository state.
2. Identify the current development phase.
3. Inspect relevant existing files.
4. Create a concise plan.
5. Implement only the required scope.
6. Test the implementation.
7. Fix errors.
8. Summarize changes.
9. Recommend the next logical step.

Prioritize a working MVP over excessive complexity.

The first objective is:

**Build a fully functional AI-powered invoice document workflow automation system with authentication, document upload, structured extraction, validation, workflow routing, human review, and analytics.**

After the MVP is stable, extend the platform to support additional document types.
