from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")

def run_financial_crew(query: str, file_path: str = "data/sample.pdf"):
    """Run the financial analysis crew"""
    try:
        # Update the task context with the file path
        task_context = {
            'query': query, 
            'file_path': file_path
        }
        
        # Create a new task instance with the file path
        analysis_task = analyze_financial_document
        analysis_task.description = analysis_task.description.format(**task_context)
        
        financial_crew = Crew(
            agents=[financial_analyst],
            tasks=[analysis_task],
            process=Process.sequential,
            verbose=True
        )
        
        result = financial_crew.kickoff(task_context)
        return result
    except Exception as e:
        raise Exception(f"Error running financial crew: {str(e)}")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Validate query
        if not query or query.strip() == "":
            query = "Analyze this financial document for investment insights"
            
        # Process the financial document
        response = run_financial_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)