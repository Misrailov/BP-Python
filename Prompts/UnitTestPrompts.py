
prompts = {
    "small_prompt":  "Write a Unit Test in the programming Language X++ for the following test case:"
                     "A comprehensive suite of unit tests for an AI chatbot should cover various aspects of the Junior Class entity. These tests should validate the integrity and functionality of attributes such as firstname, lastname, age, startingDate, and JUNLevel. Specifically, the JUNLevel attribute should be rigorously tested against expected values, including 'Analyst,' 'Consultant,' and 'SeniorConsultant.' Additionally, constraints on attributes like JunJuniorID2, which must be non-negative and numerical, should be thoroughly verified. Furthermore, the calculation of amountOfExperience, representing the duration an employee has been with the company since the starting date, should be accurately tested to ensure its correctness.",
    "medium_prompt": "Write a Unit Test in the programming language X++, commonly known as Dynamics AX or Axapta. This language is used for Dynamics 365 for Finance And Operations"
                     "always add this attribute above the function you write [SysTestMethod]"
                     "these Unit Test should be able to compile and run without problems or giving errors."
                     "The test case is described below: \n"
                     "A comprehensive suite of unit tests for an AI chatbot should cover various aspects of the Junior Class entity. These tests should validate the integrity and functionality of attributes such as firstname, lastname, age, startingDate, and JUNLevel. Specifically, the JUNLevel attribute should be rigorously tested against expected values, including 'Analyst,' 'Consultant,' and 'SeniorConsultant.' Additionally, constraints on attributes like JunJuniorID2, which must be non-negative and numerical, should be thoroughly verified. Furthermore, the calculation of amountOfExperience, representing the duration an employee has been with the company since the starting date, should be accurately tested to ensure its correctness."
                     "Here are some examples of unit tests:\n"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
    trans.getAssetCompany();\n\
}"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
    this.parmExceptionExpected(true);\n\
    trans.getAssetCompany();\n\
}"
,


    "large_prompt": "You are an X++ Unit Test Generator for Dynamics 365! Please write a Unit Test in the programming language X++ (also known as Dynamics AX or Axapta) to test a specific functionality or module within Dynamics 365 for Finance And Operations. Remember to adhere to best practices and maintain code quality.\n\
To ensure compatibility and standardization, always include the following attribute above the function you write: [SysTestMethod].\n\
\n\
Your Unit Test should be comprehensive, covering various scenarios and edge cases, to ensure robustness and reliability. Additionally, ensure that the Unit Test you write can compile and run without any errors or issues."
                    "The test case is described below: \n"
                     "A comprehensive suite of unit tests for an AI chatbot should cover various aspects of the Junior Class entity. These tests should validate the integrity and functionality of attributes such as firstname, lastname, age, startingDate, and JUNLevel. Specifically, the JUNLevel attribute should be rigorously tested against expected values, including 'Analyst,' 'Consultant,' and 'SeniorConsultant.' Additionally, constraints on attributes like JunJuniorID2, which must be non-negative and numerical, should be thoroughly verified. Furthermore, the calculation of amountOfExperience, representing the duration an employee has been with the company since the starting date, should be accurately tested to ensure its correctness."
                                         "Here are some examples of unit tests:\n"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
\n\
    this.parmExceptionExpected(true);\n\
\n\
    trans.getAssetCompany();\n\
}"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
 \n\
    trans.getAssetCompany();\n\
}"
                     "class LedgerJournalTransTest extends SysTestCase{    LedgerJournalTrans trans;}public void setUp(){super();\n\
 \n\
    // Set to non-zero values, because it one side should be zeroed// and we want to test if it happes.    trans.AmountCurDebit = 1.234;\n\
    trans.AmountCurCredit = 1.234;}[SysTestMethodAttribute]public void negativeNoCorrection(){// ACT    trans.amountCur2DebCred(-99);\n\
 \n\
    // ASSERT    this.assertEquals(0, trans.AmountCurDebit);\n\
    this.assertEquals(99, trans.AmountCurCredit);}[SysTestMethodAttribute]public void positiveNoCorrection(){// ACT    trans.amountCur2DebCred(99);\n\
 \n\
    // ASSERT    this.assertEquals(99, trans.AmountCurDebit);\n\
    this.assertEquals(0, trans.AmountCurCredit);\n\
}""Here are some examples of unit tests:\n"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
\n\
    this.parmExceptionExpected(true);\n\
\n\
    trans.getAssetCompany();\n\
}"
                     "[SysTestMethodAttribute]public void getAssetCompanyNotAssetType(){    trans.AccountType       = LedgerJournalACType::Cust;\n\
    trans.OffsetAccountType = LedgerJournalACType::Bank;\n\
 \n\
    trans.getAssetCompany();\n\
}"
                     "class LedgerJournalTransTest extends SysTestCase{    LedgerJournalTrans trans;}public void setUp(){super();\n\
 \n\
    // Set to non-zero values, because it one side should be zeroed// and we want to test if it happes.    trans.AmountCurDebit = 1.234;\n\
    trans.AmountCurCredit = 1.234;}[SysTestMethodAttribute]public void negativeNoCorrection(){// ACT    trans.amountCur2DebCred(-99);\n\
 \n\
    // ASSERT    this.assertEquals(0, trans.AmountCurDebit);\n\
    this.assertEquals(99, trans.AmountCurCredit);}[SysTestMethodAttribute]public void positiveNoCorrection(){// ACT    trans.amountCur2DebCred(99);\n\
 \n\
    // ASSERT    this.assertEquals(99, trans.AmountCurDebit);\n\
    this.assertEquals(0, trans.AmountCurCredit);\n\
}\n\
                     internal final class RetailOfflineTerminalStateTest extends SysTestCase\n\
{\n\
    /// <summary>\n\
    /// Test for validating the time gap for Last status.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void validateTimeGap()\n\
    {\n\
        // Arrange\n\
        const int OneMinute = 60;\n\
        const int OneHour = 60 * 60;\n\
        const int OneDay = 24 * 60 * 60;\n\
 \n\
        // Act\n\
 \n\
        // Assert\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(30), \"Display method message didn't match.\");\n\\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(OneMinute - 1), \"Display method message didn't match.\");\n\\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(OneMinute), \"Display method message didn't match.\");\n\\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(OneMinute + 1), \"Display method message didn't match.\");\n\\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(OneMinute + 30), \"Display method message didn't match.\");\n\\n\
        this.assertEquals('A minute ago',  RetailOfflineTerminalState::timeGap(2 * OneMinute - 1), \"Display method message didn't match.\");\n\\n\\n\
 \n\\n\\n\
        this.assertEquals('2 minutes ago', RetailOfflineTerminalState::timeGap(2 * OneMinute), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('2 minutes ago', RetailOfflineTerminalState::timeGap(2 * OneMinute + 1), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('2 minutes ago', RetailOfflineTerminalState::timeGap(3 * OneMinute - 1), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('3 minutes ago', RetailOfflineTerminalState::timeGap(3 * OneMinute), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('3 minutes ago', RetailOfflineTerminalState::timeGap(3 * OneMinute + 1), \"Display method message didn't match.\");\n\\n\\n\
 \n\\n\\n\
        this.assertEquals('40 minutes ago', RetailOfflineTerminalState::timeGap(40 * OneMinute), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('59 minutes ago', RetailOfflineTerminalState::timeGap(59 * OneMinute), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('59 minutes ago', RetailOfflineTerminalState::timeGap(OneHour - 1), \"Display method message didn't match.\");\n\\n\\n\
 \n\\n\\n\
        this.assertEquals('An hour ago', RetailOfflineTerminalState::timeGap(OneHour), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('An hour ago', RetailOfflineTerminalState::timeGap(OneHour + 1), \"Display method message didn't match.\");\n\\n\\n\
        this.assertEquals('An hour ago', RetailOfflineTerminalState::timeGap(2 * OneHour - 1), \"Display method message didn't match.\");\n\\n\\n\
 \n\\n\\n\
        this.assertEquals('2 hours ago', RetailOfflineTerminalState::timeGap(2 * OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('2 hours ago', RetailOfflineTerminalState::timeGap(2 * OneHour + 1), \"Display method message didn't match.\");\n\
        this.assertEquals('2 hours ago', RetailOfflineTerminalState::timeGap(2 * OneHour + 30 * OneMinute), \"Display method message didn't match.\");\n\
        this.assertEquals('2 hours ago', RetailOfflineTerminalState::timeGap(3 * OneHour - 1), \"Display method message didn't match.\");\n\
        this.assertEquals('3 hours ago', RetailOfflineTerminalState::timeGap(3 * OneHour), \"Display method message didn't match.\");\n\
 \n\
        this.assertEquals('10 hours ago', RetailOfflineTerminalState::timeGap(10 * OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('20 hours ago', RetailOfflineTerminalState::timeGap(20 * OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('23 hours ago', RetailOfflineTerminalState::timeGap(23 * OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('23 hours ago', RetailOfflineTerminalState::timeGap(24 * OneHour - 1), \"Display method message didn't match.\");\n\
 \n\
        this.assertEquals('A day ago', RetailOfflineTerminalState::timeGap(24 * OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('A day ago', RetailOfflineTerminalState::timeGap(OneDay + 1), \"Display method message didn't match.\");\n\
        this.assertEquals('A day ago', RetailOfflineTerminalState::timeGap(OneDay + OneHour), \"Display method message didn't match.\");\n\
        this.assertEquals('A day ago', RetailOfflineTerminalState::timeGap(2 * OneDay - 1), \"Display method message didn't match.\");\n\
 \n\
        this.assertEquals('2 days ago', RetailOfflineTerminalState::timeGap(2 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('2 days ago', RetailOfflineTerminalState::timeGap(2 * OneDay + 1), \"Display method message didn't match.\");\n\
        this.assertEquals('2 days ago', RetailOfflineTerminalState::timeGap(3 * OneDay - 1), \"Display method message didn't match.\");\n\
        this.assertEquals('3 days ago', RetailOfflineTerminalState::timeGap(3 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('3 days ago', RetailOfflineTerminalState::timeGap(3 * OneDay + 1), \"Display method message didn't match.\");\n\
        this.assertEquals('7 days ago', RetailOfflineTerminalState::timeGap(7 * OneDay), \"Display method message didn't match.\");\n\
 \n\
        this.assertEquals('30 days ago', RetailOfflineTerminalState::timeGap(30 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('300 days ago', RetailOfflineTerminalState::timeGap(300 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('999 days ago', RetailOfflineTerminalState::timeGap(3000 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('999 days ago', RetailOfflineTerminalState::timeGap(30000 * OneDay), \"Display method message didn't match.\");\n\
        this.assertEquals('999 days ago', RetailOfflineTerminalState::timeGap(300000 * OneDay), \"Display method message didn't match.\");\n\
    }\n\
 \n\
}",





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
