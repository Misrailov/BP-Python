prompts = {
    "small_prompt": "Write a display function in the programming language X++, the function description is below:"
                    "This X++ function calculates the total training cost per junior by iterating through training records matching the JunJuniorId2 of the current object. It accumulates the cost by multiplying the training duration with the price per hour for each training record. Finally, it returns the total training cost. To recreate this functionality, another AI chatbot would need to replicate the loop structure, ensure correct variable types and names, and implement the necessary data retrieval and calculation logic.",
    "medium_prompt": "Write a display function in the programming language X++, commonly known as Dynamics AX or Axapta. This language is used for Dynamics 365 for Finance And Operations"
                     "always add this attribute above the function you write [SysClientCacheDataMethodAttribute(true)]"
                     "these display functions should be able to compile and run without problems or giving errors."
                     "The function is described below: \n"
                     "This X++ function calculates the total training cost per junior by iterating through training records matching the JunJuniorId2 of the current object. It accumulates the cost by multiplying the training duration with the price per hour for each training record. Finally, it returns the total training cost. To recreate this functionality, another AI chatbot would need to replicate the loop structure, ensure correct variable types and names, and implement the necessary data retrieval and calculation logic."
                     "Here are some examples: \n"

                     "public display Name FullName() {     Name fullName = this.FirstName + this.LastName;     return fullName; }\n"
                     "public display SalesLineShowItemName itemName()     {         return this.inventTable().itemName(this.inventDim());     }\n"
                     "display LogisticsAddressing address()     {         return this.postalAddress().Address;     }\n",

    "large_prompt": "Write a display function in the programming language X++, commonly known as Dynamics AX or Axapta. This language is used for Dynamics 365 for Finance And Operations"
                    "always add this attribute above the function you write [SysClientCacheDataMethodAttribute(true)]"
                    "these display functions should be able to compile and run without problems or giving errors."
                    "               Grid Controls in Forms:\n\
Display multiple columns like strings, numbers, and enum values.\n\
Controls in the grid typically have the DataSource property set to show records from the DataSource on the form.\n\
DataField property is usually set on controls to show values stored in the DataSource field specified.\n\
Display Methods Overview:\n\
Used when the desired value isn't stored explicitly in a table field.\n\
Defined with the keyword ‘display’ in the method definition.\n\
Should return a basic data type (string, integer, real, or enum), not a class object.\n\
Best Practice: Return an EDT as the return type."
                    "The function that you should make a display function for is described below: \n"
                    "This X++ function calculates the total training cost per junior by iterating through training records matching the JunJuniorId2 of the current object. It accumulates the cost by multiplying the training duration with the price per hour for each training record. Finally, it returns the total training cost. To recreate this functionality, another AI chatbot would need to replicate the loop structure, ensure correct variable types and names, and implement the necessary data retrieval and calculation logic."
                    "Here are some examples: \n"

                    "public display Name FullName() {     Name fullName = this.FirstName + this.LastName;     return fullName; }\n"
                    "public display SalesLineShowItemName itemName()     {         return this.inventTable().itemName(this.inventDim());     }\n"
                    "display LogisticsAddressing address()     {         return this.postalAddress().Address;     }\n"
                    "  [SysClientCacheDataMethodAttribute(true)]\n\
    public static display Description jobDescription(HcmJob _this)\n\
    {\n\
        return  strFmt('%1-%2',_this.JobId, HcmJobDetail::findByJob(_this.RecId).Description);\n\
    }"
                    "/// <summary>\n\
  /// Return the names of the location roles\n\
  /// </summary>\n\
  /// <returns>\n\
  /// A string with the names of the location roles.\n\
  /// </returns>\n\
  public display DirPartyAddressLocationRoleNames locationRoles()\n\
  {\n\
      return AccountantLogistics_BR::postalLocationRoles(AccountantLogisticsLocation_BR::find(this.Accountant, this.Location));\n\
  }"
                    "[SysClientCacheDataMethod]\n\
   internal display str getJobType()\n\
   {\n\
       var jobType = '';\n\
\n\
       if (this.SourceLinkRecId)\n\
       {\n\
           jobType = enum2Str(this.Type);\n\
       }\n\
\n\
       return jobType;\n\
   }\n\
\n\
   [SysClientCacheDataMethod]\n\
   internal display str getJobStatus()\n\
   {\n\
       var jobStatus = '';\n\
\n\
       if (this.SourceLinkRecId)\n\
       {\n\
           var isSaveToHistoryJob = this.isSaveToHistoryJob();\n\
\n\
           if (this.Status == ArchiveServiceJobStatus::Ready ||\n\
               this.Status == ArchiveServiceJobStatus::Error)\n\
           {\n\
               jobStatus = enum2Str(this.Status);\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Archived)\n\
           {\n\
               jobStatus = isSaveToHistoryJob\n\
                   ? \"@ArchiveService:ArchiveServiceJobStatusArchived\"\n\
                   : \"@ArchiveService:ArchiveJobStatusRestored\";\n\
           }\n\
           else\n\
           {\n\
               jobStatus = \"@ArchiveService:ArchiveJobInProgressStatusOnWorkSpace\";\n\
           }\n\
       }\n\
\n\
       return jobStatus;\n\
   }\n\
\n\
   [SysClientCacheDataMethod]\n\
   internal display container getJobStatusIcon()\n\
   {\n\
       var jobStatusIconContainer = conNull();\n\
\n\
       if (this.SourceLinkRecId && this.Status != ArchiveServiceJobStatus::Unknown)\n\
       {\n\
           str jobStatusImage = ImageReferenceSymbol::Refresh;\n\
\n\
           if (this.Status == ArchiveServiceJobStatus::Archived)\n\
           {\n\
               jobStatusImage = ImageReferenceSymbol::GreenCheck;\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Error)\n\
           {\n\
               jobStatusImage = ImageReferenceSymbol::Error;\n\
           }\n\
\n\
           jobStatusIconContainer = ImageReference::constructForSymbol(jobStatusImage).pack();\n\
       }\n\
\n\
       return jobStatusIconContainer;\n\
   }\n\
\n\
   [SysClientCacheDataMethod]\n\
   internal display str getJobProcessingProgressStatus()\n\
   {\n\
       var progressStatus = '';\n\
\n\
       if (this.SourceLinkRecId)\n\
       {\n\
           var isSaveToHistoryJob = this.isSaveToHistoryJob();\n\
           var totalRecordsProcessed = num2Str(this.TotalRecordsProcessed, -1, 0, -1, -1);\n\
\n\
           if (this.Status == ArchiveServiceJobStatus::CompletedMoveToLongTermRetention)\n\
           {\n\
               progressStatus = \"@ArchiveService:ArchiveCompletedLongTermRetentionResults\";\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Archived)\n\
           {\n\
               progressStatus = isSaveToHistoryJob\n\
                   ? strFmt(\"@ArchiveService:ArchiveServiceJobProgressCompletedStatus\", totalRecordsProcessed)\n\
                   : strFmt(\"@ArchiveService:ArchiveJobResultsRestored\", totalRecordsProcessed);\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Error)\n\
           {\n\
               progressStatus = isSaveToHistoryJob\n\
                   ? strFmt(\"@ArchiveService:ArchiveServiceResultsFailure\")\n\
                   : strFmt(\"@ArchiveService:ArchiveJobResultsRestoreFailed\");\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Executing)\n\
           {\n\
               // If job progress is greater than 50%, the job has completing staging and has begun moving of records\n\
               if (this.PercentageComplete >= 50)\n\
               {\n\
                   var totalRecordsToProcess = num2Str(this.TotalRecordsToProcess, -1, 0, -1, -1);\n\
\n\
                   progressStatus = isSaveToHistoryJob\n\
                       ? strFmt(\"@ArchiveService:ArchiveJobResultsSavingToHistory\", totalRecordsProcessed, totalRecordsToProcess)\n\
                       : strFmt(\"@ArchiveService:ArchiveJobResultsRestoring\", totalRecordsProcessed, totalRecordsToProcess);\n\
               }\n\
               else\n\
               {\n\
                   // If the job progress is less than 50%, the job is still staging records to be moved\n\
                   progressStatus = \"@ArchiveService:ArchiveServiceJobProgressStagingStatus\";\n\
               }\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::Ready ||\n\
                    this.Status == ArchiveServiceJobStatus::Unknown)\n\
           {\n\
               progressStatus = isSaveToHistoryJob\n\
                   ? \"@ArchiveService:ArchiveServiceJobWaitingToProcess\"\n\
                   : \"@ArchiveService:ArchiveJobStatusWaitingToRestore\";\n\
           }\n\
           else if (this.Status == ArchiveServiceJobStatus::MovingToLongTermRetention)\n\
           {\n\
               progressStatus = \"@ArchiveService:ArchiveViewProgress\";\n\
           }\n\
       }\n\
\n\
       return progressStatus;\n\
   }\n\
\n\
   [SysClientCacheDataMethod]\n\
   internal display str getJobResultsLink()\n\
   {\n\
       var jobResultsLink = '';\n\
\n\
       // Only show the view job results link if the source link is associated with an actively executing job\n\
       if (this.SourceLinkRecId && this.Status != ArchiveServiceJobStatus::Unknown)\n\
       {\n\
           jobResultsLink = \"@ArchiveService:ArchiveJobResultsLink\";\n\
       }\n\
\n\
       return jobResultsLink;\n\
   }"
                    " The function that you should make a display function for is described below: \n"
                    "This X++ function calculates the total training cost per junior by iterating through training records matching the JunJuniorId2 of the current object. It accumulates the cost by multiplying the training duration with the price per hour for each training record. Finally, it returns the total training cost. To recreate this functionality, another AI chatbot would need to replicate the loop structure, ensure correct variable types and names, and implement the necessary data retrieval and calculation logic."
    ,

    "system_small_prompt": "You are an expert in the programming language X++.",
    "system_medium_prompt": "You are an expert in the programming language X++ used for Dynamics 365 Finance And "
                            "Operations, you know every piece of code and are very knowledgeable. You always remember "
                            "that you are coding in the X++ programing Language. You only return code, you don't give "
                            "explanations.",
    "system_large_prompt": "Here's the expanded system_message for your AI chatbot:\n\
You are an expert in the programming language X++ used for Dynamics 365 Finance And Operations. You have extensive knowledge of the X++ syntax, data types, control structures, classes, methods, and best practices specific to this language and the Dynamics 365 environment.\n\
Your role is to generate code snippets and complete solutions in response to user requests, focusing solely on providing accurate and efficient X++ code. You understand the intricacies of integrating with the Dynamics 365 platform, including the use of its APIs, frameworks, and libraries.\n\
When generating code, always ensure that it adheres to the X++ language specifications and follows the recommended coding conventions and standards. Take into account performance optimization techniques, error handling, and security considerations relevant to the Dynamics 365 ecosystem.\n\
Remember to tailor your code generation to the specific requirements provided by the user, considering factors such as data models, business logic, and user interface interactions within the Dynamics 365 application.\n\
You should only respond with the generated X++ code and avoid providing explanations or additional commentary. Your responses should be concise, focusing solely on the code itself.\n\
Your ultimate goal is to assist users in developing efficient and effective X++ solutions for Dynamics 365 Finance and Operations by providing them with accurate and well-structured code snippets."
}
