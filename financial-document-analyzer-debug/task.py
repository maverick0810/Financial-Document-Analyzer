## Importing libraries and files
from crewai import Task
from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

## Creating a comprehensive financial document analysis task
analyze_financial_document = Task(
    description="""Conduct a thorough analysis of the financial document to address the user's query: {query}
    
    Your analysis should include:
    1. Read and comprehensively analyze the provided financial document using the read_data_tool
    2. Extract key financial metrics, ratios, and performance indicators
    3. Identify trends, strengths, and areas of concern
    4. Provide data-driven insights relevant to the user's specific query
    5. Ensure all analysis is based on factual information from the document
    6. Follow professional financial analysis standards and best practices
    
    Use the file_path parameter if provided, otherwise use the default sample file.""",

    expected_output="""Provide a comprehensive financial analysis report including:
    - Executive summary of key findings
    - Detailed financial metrics analysis (revenue, profit margins, debt ratios, etc.)
    - Risk assessment and identification of potential concerns
    - Investment insights and recommendations based on the data
    - Clear, professional conclusions supported by evidence from the financial document
    - Proper financial terminology and regulatory compliance considerations
    
    Format the output in a clear, structured manner suitable for professional financial reporting.""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="""Analyze the financial document to provide investment recommendations based on the user query: {query}
    
    Focus on:
    1. Financial performance metrics and trends from the document
    2. Market position and competitive advantages
    3. Revenue growth and profitability analysis
    4. Balance sheet strength and debt management
    5. Cash flow analysis and dividend potential
    6. Investment risks and opportunities""",

    expected_output="""Provide professional investment analysis including:
    - Investment thesis based on financial data from the document
    - Key performance indicators and their implications
    - Risk-return assessment
    - Portfolio fit and investment timeline considerations
    - Regulatory and compliance factors
    - Clear investment recommendation with supporting rationale from the financial data""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="""Conduct comprehensive risk assessment based on the financial document and user query: {query}
    
    Analyze:
    1. Financial risks (credit, liquidity, market, operational) from the document
    2. Business model sustainability based on financial data
    3. Industry and competitive risks evident in the financials
    4. Regulatory and compliance risks
    5. ESG (Environmental, Social, Governance) considerations
    6. Macroeconomic sensitivity based on financial performance""",

    expected_output="""Deliver a professional risk assessment report:
    - Risk categorization and prioritization based on document analysis
    - Quantitative and qualitative risk metrics from financial data
    - Risk mitigation strategies and recommendations
    - Stress testing scenarios and sensitivity analysis
    - Risk monitoring and early warning indicators
    - Compliance with risk management best practices""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a document verification task
verification = Task(
    description="""Verify the authenticity and completeness of the financial document for query: {query}
    
    Check for:
    1. Document structure and format consistency
    2. Presence of required financial statements
    3. Data integrity and logical consistency
    4. Regulatory compliance markers
    5. Audit trail and verification elements""",

    expected_output="""Provide document verification report:
    - Document authenticity assessment
    - Completeness checklist results
    - Data quality and integrity evaluation
    - Identified discrepancies or concerns
    - Verification confidence level
    - Recommendations for additional verification if needed""",

    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)