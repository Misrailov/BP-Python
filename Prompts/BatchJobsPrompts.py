
prompts = {
    "small_prompt": "Write a batch job in the programming Language X++, commonly known as Dynamics AX, the function "
                    "of the batch job is described below:The class above updates records in a table called "
                    "JunTrainingTable2 where the EndDate is before today and the Completed field is false, "
                    "setting the Completed field to true. It then displays a message indicating the number of records "
                    "that were updated or a warning if no records were updated.  n ",
    "medium_prompt": "Write batch jobs using the SysOperation framework in the Language X++ or also    "
                     "\nknows as Dynamics AX and Axapta, this language is used for Dynamics 365 for finance and operations,  "
                     "\nthese batch jobs with the Sysoperation Framework should run without giving me error codes, "
                     "these batch"
                     "  \nnjobs using the SysOperation Framework should fulfill the function i provided. "
                     "nThe classes i Want is the contract class with the [DataContractAttribute], the Service class "
                     "which has the main functionality and extends the    nSysOperationServiceBase, the last class I "
                     "want is the Controller class which extends the SysOperationServiceController.   nIn the "
                     "Controller class configures the SysOperation Framework process Dont forget to think step by "
                     "step.  n   nIf you forget something about how dates work in X++ use this link:  "
                     "”https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-date-run-time"
                     "-functions  ”   nFor more general information about X++ look at these links:  "
                     "”https://learn.microsoft.com/en-us/dynamicsax-2012/developer/x-language-programming-guide  ”    "
                     "nYou can also look at these:   ”https://dynamics365musings.com/  ”   n  nThe function which the "
                     "batch job should accomplish   is this \n  : The class above updates records in a table called "
                     "JunTrainingTable2 where the EndDate is before today and the Completed field is false, "
                     "setting the Completed field to true. It then displays a message indicating the number of "
                     "records that were updated or a warning if no records were updated.  \nThis is an example of "
                     "what a batch job could look like:  \n [SysOperationJournaledParametersAttribute(true)]\npublic "
                     "class SMROCRequestLogCleanupController extends SysOperationServiceController\n{\n    \n    "
                     "public static void main(Args _args)\n    {\n        SMROCRequestLogCleanupController controller "
                     "=\n            SMROCRequestLogCleanupController::construct();\n        controller.parmArgs("
                     "_args);\n        controller.startOperation();\n    }\n\n    public static "
                     "SMROCRequestLogCleanupController construct(\n        SysOperationExecutionMode _executionMode "
                     "=\n            SysOperationExecutionMode::Synchronous)\n    {\n        "
                     "SMROCRequestLogCleanupController controller =\n            new "
                     "SMROCRequestLogCleanupController();\n        controller.parmExecutionMode(_executionMode);\n    "
                     "    return controller;\n    }\n\n    protected void new()\n    {\n        super(classStr("
                     "SMROCRequestLogCleanupService),\n            methodStr(SMROCRequestLogCleanupService,"
                     "\n                cleanRequestsLog),\n            SysOperationExecutionMode::Synchronous);\n    "
                     "}\n\n}\npublic class SMROCRequestLogCleanupService\n{\n    private void addDynamicRanges("
                     "QueryBuildDataSource _qbd, SMROCRequestLogCleanupDataContract _dataContract)\n    {\n        "
                     "QueryBuildRange qbr; \n        if (_dataContract.parmHttpResponsCode())\n        {\n            "
                     "qbr = _qbd.addRange(fieldNum(SMROCRequestLog,HttpResponseCode));\n            qbr.value("
                     "_dataContract.parmHttpResponsCode());\n        }\n\n        if (_dataContract.parmSuccesError("
                     "))\n        {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog, SuccessError));\n      "
                     "      qbr.value(enum2Str(_dataContract.parmSuccesError()));\n        }\n\n        if ("
                     "_dataContract.parmUserId())\n        {\n            qbr = _qbd.addRange(fieldNum("
                     "SMROCRequestLog, User));\n            qbr.value(_dataContract.parmUserId());\n        }\n\n     "
                     "   if (_dataContract.parmFileName())\n        {\n            qbr = _qbd.addRange(fieldNum("
                     "SMROCRequestLog, Filename));\n            qbr.value(_dataContract.parmFileName());\n        "
                     "}\n\n        if (_dataContract.parmNumbOfDays())\n        {\n            qbr = _qbd.addRange("
                     "fieldNum(SMROCRequestLog,ActionDate2 )); \n            qbr.value("
                     "SysQueryRangeUtil::lessThanDate(-_dataContract.parmNumbOfDays())); //toTest\n        }\n\n      "
                     "  if (_dataContract.parmRequestLocation())\n        {\n            qbr = _qbd.addRange("
                     "fieldNum(SMROCRequestLog, RequestLocation));\n            qbr.value(enum2Str("
                     "_dataContract.parmRequestLocation()));\n        }\n\n        if (_dataContract.parmReportName("
                     "))\n        {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog, ReportName));\n        "
                     "    qbr.value(_dataContract.parmReportName());\n        }\n\n    }\n\n    private void "
                     "performCleanup(Query _q)\n    {\n        QueryRun qr = new QueryRun(_q);\n        "
                     "SMROCRequestLog requestLog;\n        int counter = 0; \n\n        ttsbegin;\n        while( "
                     "qr.next())\n        {\n            counter++; \n            requestLog  = qr.get(tablenum("
                     "SMROCRequestLog));\n            requestLog.delete();\n        }\n        ttscommit;\n\n        "
                     "if (counter > 0) \n        {\n            Info(strFmt(\"@SMROC:SMROC75\", counter)); \n        "
                     "}\n    }\n\n    public void cleanRequestsLog(\n        SMROCRequestLogCleanupDataContract "
                     "_dataContract)\n    {\n        Query q;\n        QueryBuildDataSource qbd;\n        q = new "
                     "Query();\n        qbd = q.addDataSource(TableNum(SMROCRequestLog));\n        qbd.update("
                     "true);\n\n\n        this.addDynamicRanges(qbd,_dataContract);\n        this.performCleanup("
                     "q);\n    }\n\n}\n[DataContractAttribute]\npublic class SMROCRequestLogCleanupDataContract\n{\n  "
                     "  protected SMROCHttpResponseCode httpResponsCode;\n    protected UserSuccessError "
                     "succesError;\n    protected UserId userId;\n    protected Filename fileName;\n    protected "
                     "SMROCNumOfDays numbOfDays;\n    protected SMROCRequestlocations requestLocation;\n    protected "
                     "SMROCReportName reportName;  \n\n    [DataMemberAttribute]\n    public SMROCHttpResponseCode  "
                     "parmHttpResponsCode(SMROCHttpResponseCode _httpResponsCode = httpResponsCode)\n    {\n        "
                     "httpResponsCode =  _httpResponsCode;\n        return httpResponsCode;\n    }\n\n    ["
                     "DataMemberAttribute]\n    public UserSuccessError parmSuccesError(UserSuccessError _succesError "
                     "= succesError )\n    {\n        succesError= _succesError;\n        return succesError;\n    "
                     "}\n\n    [DataMemberAttribute]\n    public UserId parmUserId(UserId _userId = userId )\n    {\n "
                     "       userId = _userId;\n        return userId;\n    }\n\n    [DataMemberAttribute]\n    "
                     "public Filename parmFileName(Filename _fileName = fileName )\n    {\n        fileName = "
                     "_fileName;\n        return fileName;\n    }\n\n    [DataMemberAttribute]\n    public "
                     "SMROCRequestlocations  parmRequestLocation(SMROCRequestlocations _requestLocation = "
                     "requestLocation)\n    {\n        requestLocation =  _requestLocation;\n        return "
                     "requestLocation;\n    }\n\n    [DataMemberAttribute]\n    public SMROCNumOfDays  "
                     "parmNumbOfDays(SMROCNumOfDays _numbOfDays = numbOfDays)\n    {\n        numbOfDays =  "
                     "_numbOfDays;\n        return numbOfDays;\n    }\n\n    [DataMemberAttribute]\n    public "
                     "SMROCReportName  parmReportName(SMROCReportName _reportName = reportName)\n    {\n        "
                     "reportName =  _reportName;\n        return reportName;\n    }\n\n}\n//example2\n/// "
                     "<summary>\n/// Controller class containing specific Sales Reservation logic\n/// </summary>\n["
                     "SysOperationJournaledParametersAttribute(true)]\npublic class "
                     "SMRRBSalesReservationServiceController extends SysOperationServiceController\n{\n    protected "
                     "void new()\n    {\n        super();\n\n        this.parmClassName(classStr("
                     "SMRRBSalesReservationService));\n        this.parmMethodName(methodStr("
                     "SMRRBSalesReservationService, processOperation));\n    \n        this.parmDialogCaption("
                     "\"@SMRRB:SMRRB005\");\n\n    }\n\n    public static SMRRBSalesReservationServiceController "
                     "construct()\n    {\n        SMRRBSalesReservationServiceController controller = new "
                     "SMRRBSalesReservationServiceController();\n\n        return controller;\n    }\n\n    public "
                     "static void main(Args _args)\n    {\n        SMRRBSalesReservationServiceController controller "
                     "= SMRRBSalesReservationServiceController::construct();\n        "
                     "SMRRBSalesReservationDataContract dataContract = controller.getDataContractObject();\n\n        "
                     "dataContract.parmTimeFence(SMRRBParameters::find().SalesReservationsTimeFence);\n\n        "
                     "controller.parmExecutionMode(SysOperationExecutionMode::Synchronous);\n        "
                     "controller.parmLoadFromSysLastValue(false);\n\n        controller.startOperation();\n    }\n\n  "
                     "  protected boolean validate()\n    {\n        return true;\n    }\n\n    public void run()\n   "
                     " {\n        super();\n    }\n\n}\n/// <summary>\n/// SysOperation-framework uses this extended "
                     "class to execute the sales reservation batch logic\n/// </summary>\npublic class "
                     "SMRRBSalesReservationService extends SysOperationServiceBase\n{\n    "
                     "SMRRBSalesReservationDataContract dataContract;\n\n    /// <summary>\n    /// The main service "
                     "method\n    /// </summary>\n    /// <param name = \"_dataContract\">\n    /// contract "
                     "containing all the input parameters for the batch\n    /// </param>\n    public void "
                     "processOperation(SMRRBSalesReservationDataContract _dataContract)\n    {\n        "
                     "SMRRBSalesReservation salesReservation = SMRRBSalesReservation::construct("
                     "_dataContract.getQuery(), _dataContract.parmTimeFence());\n        salesReservation.run();\n    "
                     "}\n\n}\n/// <summary>\n/// Extension of the SMRRBReservationDataContract that specifies the "
                     "input values for the SalesLine reservation batch\n/// </summary>\n[DataContractAttribute, "
                     "SysOperationContractProcessingAttribute(classStr(SMRRBSalesReservationUIBuilder))]\npublic "
                     "class SMRRBSalesReservationDataContract extends SMRRBReservationDataContract\n{\n    ["
                     "DataMemberAttribute, AifQueryTypeAttribute(\"_packedQuery\", queryStr("
                     "SMRRBSalesReservation))]\n    public str parmQuery(str _packedQuery = packedQuery)\n    {\n     "
                     "   packedQuery = _packedQuery;\n        return packedQuery;\n    }\n\n}",


    "large_prompt": "\n\
To create batch jobs using the SysOperation framework in X++, also known as Dynamics AX and Axapta, you'll want to ensure a smooth execution without encountering error codes. Follow these steps to craft efficient and error-free batch jobs:\n\
Understand the SysOperation Framework: Familiarize yourself with the SysOperation framework, which provides a structured way to create batch processes in X++. This framework helps in creating contracts, services, and controllers for batch jobs.\n\
Define Contract Class: Start by defining a contract class with the [DataContractAttribute] annotation. This class will define the parameters and data members that will be passed between the client and the service. In your contract class, clearly outline the parameters required for the batch job, ensuring that all necessary information is included for seamless execution.\n\
Implement Service Class: Next, implement the service class. This class contains the main functionality of your batch job and extends the SysOperationServiceBase class. Ensure that the service class handles the business logic efficiently and error-free. Incorporate error handling mechanisms within the service class to gracefully manage any unexpected issues that may arise during batch job execution.\n\
Create Controller Class: Now, create the controller class, which extends the SysOperationServiceController. The controller class configures the SysOperation framework process and orchestrates the execution of the batch job. Within the controller class, define methods for initializing the batch job, starting the process, and handling completion events.\n\
Configure Batch Job Process: Within the controller class, configure the SysOperation framework process. Define how the parameters are passed, specify the execution behavior, and handle any exceptional cases gracefully. Implement mechanisms for logging job progress and capturing any errors encountered during execution.\n\
Handle Dates in X++: If your batch job involves handling dates, ensure you understand how dates work in X++. Refer to Microsoft's documentation on X++ date and time functions for guidance on manipulating dates efficiently. Utilize built-in X++ date functions to perform date calculations, comparisons, and conversions within your batch job code.\n\
Testing and Debugging: Thoroughly test your batch job to ensure it fulfills the function you provided. Debug any issues that arise during testing and refine your code for optimal performance. Utilize debugging tools provided by the X++ development environment to identify and troubleshoot any errors or unexpected behavior.\n\
Optimization: Look for opportunities to optimize your batch job code. This could involve optimizing queries, minimizing resource usage, or improving algorithm efficiency. Profile your batch job code to identify performance bottlenecks and implement optimizations to enhance overall execution speed and resource utilization.\n\
Documentation: Document your batch job code thoroughly. Include comments explaining the purpose of each class, method, and significant code block. Clear documentation will help future developers understand and maintain the code. Additionally, provide instructions on how to configure and execute the batch job within the Dynamics 365 environment.\n\
Continuous Learning: Stay updated with the latest developments in X++ and the SysOperation framework. Explore online resources, forums, and community websites to learn new techniques and best practices for batch job development in X++. Attend training sessions and workshops to enhance your skills and stay abreast of industry trends.\n\
Main Method:\n\
To start, scroll down to the ‘main’ method. This method is called when the user clicks the Menu Item that points to the Batch job. Specifically, after creating a batch job class, you need to create a Menu Item, and set the Object Type to ‘Class’, and Object to the name of the class.\n\
Run Method:\n\
Next, locate the ‘run’ method in your class. The purpose of this method is to perform the task or process that your batch job should do. There are not any requirements relating to this method. However, typically this class will look through a Query object that was created in the Application Explorer. Or, it will have a while select statement that will loop through records.\n\
Common Patterns:\n\
While there are no ‘rules’ relating to what code is run in a batch job, there are a few common design patterns. Ideally, when a batch job is run, it should perform some action, such that if the same batch job is run again, it would not process the same records a second time.\n\
\n\
Parameters:\n\
Often, users will want to control what to provide input on what records are processed. For example, by giving a start and end date. Or a value of a field that should be used to filter the records to be processed. Or even the number of days in the past to keep data.\n\
Class Variables:\n\
Although class variables can be added anywhere in a class, it is a best practice to add them at the top, right after the class definition.\n\
\n\
Dialog Method:\n\
This method is responsible for adding controls to the dialog form that is shown to the user.\n\
\n\
GetFromDialog Method:\n\
Correspondingly, the getFromDialog is called after the user presses the ‘ok’ button on the dialog form. It is responsible for reading the values out of the dialog controls, and storing them into class variables. The class variables can then be used by the ‘run’ method.\n\
\n\
Pack, Unpack, a Macro:\n\
Whenever a batch job runs in batch, and it has parameters, the system needs to store the values the user entered as parameters. That way, the system can use them again, when the batch job recurrence causes it to run.\n\
\n\
Description:\n\
The description method is used to set the default task description of this batch job. This text is shown in a field in the dialog form.\n\
\n\
Other Methods:\n\
There are additional methods that can be implemented in the batch job class. Therefore, the methods mentioned here are optional. And you do not need to add them in if you do not need them.\n\
\n\
Adding A Menu Item:\n\
After creating a batch job, create a Menu Item that points to the batch job class you just created. As a best practice, all Menu Items that call batch jobs should be Action Menu Items.\n \
        \n \
        By following these steps and leveraging resources like Microsoft's documentation and community forums, "
                    "you can efficiently create batch jobs using the SysOperation framework in X++ "
                    "for Dynamics 365 for Finance and Operations. With careful planning, "
                    "thorough testing, and continuous improvement, you can develop robust "
                    "batch jobs that streamline business processes and enhance system "
                    "performance.The function which the batch job should accomplish   "
                    "is this \n  : "
                    "The class above updates records in a table called JunTrainingTable2 where the"
                    " EndDate is before today and the Completed field is false, setting "
                    "the Completed field to true. It then displays a message indicating"
                    " the number of records that were updated or a warning if no records were updated.  "
                    "\nThis is an example of what a batch job could look like:  "
                    "\n [SysOperationJournaledParametersAttribute(true)]\npublic class SMROCRequestLogCleanupController "
                    "extends SysOperationServiceController\n{\n    \n    public static void main(Args _args)\n    {\n   "
                    "     SMROCRequestLogCleanupController controller =\n            SMROCRequestLogCleanupController::construct();\n"
                    "        controller.parmArgs(_args);\n        controller.startOperation();\n    }\n\n   "
                    " public static SMROCRequestLogCleanupController construct(\n        SysOperationExecutionMode _executionMode =\n"
                    "           SysOperationExecutionMode::Synchronous)\n    {\n        SMROCRequestLogCleanupController controller =\n "
                    "           new SMROCRequestLogCleanupController();\n        controller.parmExecutionMode(_executionMode);\n    "
                    "    return controller;\n    }\n\n    protected void new()\n    {\n      "
                    "  super(classStr(SMROCRequestLogCleanupService),\n            methodStr(SMROCRequestLogCleanupService,\n    "
                    "            cleanRequestsLog),\n            SysOperationExecutionMode::Synchronous);\n   "
                    " }\n\n}\npublic class SMROCRequestLogCleanupService\n{\n   "
                    " private void addDynamicRanges(QueryBuildDataSource _qbd, SMROCRequestLogCleanupDataContract _dataContract)\n  "
                    "  {\n        QueryBuildRange qbr; \n        if (_dataContract.parmHttpResponsCode())\n        {\n "
                    "           qbr = _qbd.addRange(fieldNum(SMROCRequestLog,HttpResponseCode));\n            "
                    "qbr.value(_dataContract.parmHttpResponsCode());\n        }\n\n        if (_dataContract.parmSuccesError())\n   "
                    "     {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog, SuccessError));\n        "
                    "    qbr.value(enum2Str(_dataContract.parmSuccesError()));\n        }\n\n        if (_dataContract.parmUserId())\n  "
                    "      {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog, User));\n          "
                    "  qbr.value(_dataContract.parmUserId());\n        }\n\n        if (_dataContract.parmFileName())\n  "
                    "      {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog, Filename));\n          "
                    "  qbr.value(_dataContract.parmFileName());\n        }\n\n        if (_dataContract.parmNumbOfDays())\n     "
                    "   {\n            qbr = _qbd.addRange(fieldNum(SMROCRequestLog,ActionDate2 )); \n       "
                    "     qbr.value(SysQueryRangeUtil::lessThanDate(-_dataContract.parmNumbOfDays())); //toTest\n "
                    "       }\n\n        if (_dataContract.parmRequestLocation())\n        {\n        "
                    "    qbr = _qbd.addRange(fieldNum(SMROCRequestLog, RequestLocation));\n     "
                    "       qbr.value(enum2Str(_dataContract.parmRequestLocation()));\n        }\n\n     "
                    "   if (_dataContract.parmReportName())\n        {\n        "
                    "    qbr = _qbd.addRange(fieldNum(SMROCRequestLog, ReportName));\n      "
                    "      qbr.value(_dataContract.parmReportName());\n    "
                    "    }\n\n    }\n\n    private void performCleanup(Query _q)\n    {\n  "
                    "      QueryRun qr = new QueryRun(_q);\n        SMROCRequestLog requestLog;\n    "
                    "    int counter = 0; \n\n        ttsbegin;\n        while( qr.next())\n        {\n     "
                    "       counter++; \n            requestLog  = qr.get(tablenum(SMROCRequestLog));\n            "
                    "requestLog.delete();\n        }\n        ttscommit;\n\n        if (counter > 0) \n        {\n       "
                    "     Info(strFmt(\"@SMROC:SMROC75\", counter)); \n        }\n    }\n\n    public void cleanRequestsLog(\n        SMROCRequestLogCleanupDataContract _dataContract)\n    {\n        Query q;\n        QueryBuildDataSource qbd;\n        q = new Query();\n        qbd = q.addDataSource(TableNum(SMROCRequestLog));\n        qbd.update(true);\n\n\n        this.addDynamicRanges(qbd,_dataContract);\n        this.performCleanup(q);\n    }\n\n}\n[DataContractAttribute]\npublic class SMROCRequestLogCleanupDataContract\n{\n    protected SMROCHttpResponseCode httpResponsCode;\n    protected UserSuccessError succesError;\n    protected UserId userId;\n    protected Filename fileName;\n    protected SMROCNumOfDays numbOfDays;\n    protected SMROCRequestlocations requestLocation;\n    protected SMROCReportName reportName;  \n\n    [DataMemberAttribute]\n    public SMROCHttpResponseCode  parmHttpResponsCode(SMROCHttpResponseCode _httpResponsCode = httpResponsCode)\n    {\n        httpResponsCode =  _httpResponsCode;\n        return httpResponsCode;\n    }\n\n    [DataMemberAttribute]\n    public UserSuccessError parmSuccesError(UserSuccessError _succesError = succesError )\n    {\n        succesError= _succesError;\n        return succesError;\n    }\n\n    [DataMemberAttribute]\n    public UserId parmUserId(UserId _userId = userId )\n    {\n        userId = _userId;\n        return userId;\n    }\n\n    [DataMemberAttribute]\n    public Filename parmFileName(Filename _fileName = fileName )\n    {\n        fileName = _fileName;\n        return fileName;\n    }\n\n    [DataMemberAttribute]\n    public SMROCRequestlocations  parmRequestLocation(SMROCRequestlocations _requestLocation = requestLocation)\n    {\n        requestLocation =  _requestLocation;\n        return requestLocation;\n    }\n\n    [DataMemberAttribute]\n    public SMROCNumOfDays  parmNumbOfDays(SMROCNumOfDays _numbOfDays = numbOfDays)\n    {\n        numbOfDays =  _numbOfDays;\n        return numbOfDays;\n    }\n\n    [DataMemberAttribute]\n    public SMROCReportName  parmReportName(SMROCReportName _reportName = reportName)\n    {\n        reportName =  _reportName;\n        return reportName;\n    }\n\n}\n//example2\n/// <summary>\n/// Controller class containing specific Sales Reservation logic\n/// </summary>\n[SysOperationJournaledParametersAttribute(true)]\npublic class SMRRBSalesReservationServiceController extends SysOperationServiceController\n{\n    protected void new()\n    {\n        super();\n\n        this.parmClassName(classStr(SMRRBSalesReservationService));\n        this.parmMethodName(methodStr(SMRRBSalesReservationService, processOperation));\n    \n        this.parmDialogCaption(\"@SMRRB:SMRRB005\");\n\n    }\n\n    public static SMRRBSalesReservationServiceController construct()\n    {\n        SMRRBSalesReservationServiceController controller = new SMRRBSalesReservationServiceController();\n\n        return controller;\n    }\n\n    public static void main(Args _args)\n    {\n        SMRRBSalesReservationServiceController controller = SMRRBSalesReservationServiceController::construct();\n        SMRRBSalesReservationDataContract dataContract = controller.getDataContractObject();\n\n        dataContract.parmTimeFence(SMRRBParameters::find().SalesReservationsTimeFence);\n\n        controller.parmExecutionMode(SysOperationExecutionMode::Synchronous);\n        controller.parmLoadFromSysLastValue(false);\n\n        controller.startOperation();\n    }\n\n    protected boolean validate()\n    {\n        return true;\n    }\n\n    public void run()\n    {\n        super();\n    }\n\n}\n/// <summary>\n/// SysOperation-framework uses this extended class to execute the sales reservation batch logic\n/// </summary>\npublic class SMRRBSalesReservationService extends SysOperationServiceBase\n{\n    SMRRBSalesReservationDataContract dataContract;\n\n    /// <summary>\n    /// The main service method\n    /// </summary>\n    /// <param name = \"_dataContract\">\n    /// contract containing all the input parameters for the batch\n    /// </param>\n    public void processOperation(SMRRBSalesReservationDataContract _dataContract)\n    {\n        SMRRBSalesReservation salesReservation = SMRRBSalesReservation::construct(_dataContract.getQuery(), _dataContract.parmTimeFence());\n        salesReservation.run();\n    }\n\n}\n/// <summary>\n/// Extension of the SMRRBReservationDataContract that specifies the input values for the SalesLine reservation batch\n/// </summary>\n[DataContractAttribute, SysOperationContractProcessingAttribute(classStr(SMRRBSalesReservationUIBuilder))]\npublic class SMRRBSalesReservationDataContract extends SMRRBReservationDataContract\n{\n    [DataMemberAttribute, AifQueryTypeAttribute(\"_packedQuery\", queryStr(SMRRBSalesReservation))]\n    public str parmQuery(str _packedQuery = packedQuery)\n    {\n        packedQuery = _packedQuery;\n        return packedQuery;\n    }\n\n}",




    "system_small_prompt": "You are an expert in the programming language X++.",



    "system_medium_prompt": "You are an expert in the programming language X++ used for Dynamics 365 Finance And "
                            "Operations, you know every piece of code and are very knowledgeable. You always remember "
                            "that you are coding in the X++ programing Language. You only return code, you don't give "
                            "explanations. Above every class of code you write    <ClassBegin>    and after every "
                            "class you write </ClassEnd>.",


    "system_large_prompt": "You are an expert in the programming language X++ used for Dynamics 365 Finance And Operations. As you delve into coding, keep in mind the nuances and specific syntax of X++. Your expertise spans every aspect of this language, from basic constructs to advanced techniques.\n\
When generating code, maintain a keen focus on X++ conventions and best practices. This ensures that your code is not only functional but also follows industry standards and is easily understandable by other X++ developers.\n\
Always remember the context in which X++ is used, particularly within Dynamics 365 Finance And Operations. Consider the integration points, data models, and business logic intricacies specific to this environment.\n\
As you generate code, adhere to a structured approach. Break down complex tasks into smaller, manageable steps, and tackle them sequentially. This not only facilitates efficient coding but also helps in debugging and maintenance.\n\
Pay close attention to error handling and exception management in your code snippets. X++ offers various mechanisms for handling errors gracefully, such as try-catch blocks and exception classes. Ensure that your generated code includes robust error-handling mechanisms to enhance reliability and stability.\n\
Incorporate reusable components and modular design principles wherever possible. X++ supports object-oriented programming paradigms, allowing you to create classes, methods, and interfaces for encapsulating functionality. Leverage these features to promote code reusability and maintainability.\n\
Maintain consistency in your coding style and naming conventions throughout the generated codebase. Consistent formatting and naming improve code readability and contribute to a cohesive development environment.\n\
Remember to document your code effectively, both within the code itself and through external documentation files. Clear and concise documentation enhances the understandability of your codebase and assists other developers in utilizing and extending your work.\n\
\n\
Upon completion of code generation, encapsulate the entire code snippet within <ClassBegin> and </ClassEnd> tags. This delineates the boundaries of individual classes, making it easier to identify and manage code segments within larger projects.\n\
By adhering to these guidelines and leveraging your expertise in X++, you can consistently generate high-quality code tailored to the requirements of Dynamics 365 Finance And Operations."
  }
