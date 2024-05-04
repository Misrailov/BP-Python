
prompts = {
    "small_prompt": "Write a batch job in the programming Language X++, commonly known as Dynamics AX, the function of the batch job is described below:The class above updates records in a table called JunTrainingTable2 where the EndDate is before today and the Completed field is false, setting the Completed field to true. It then displays a message indicating the number of records that were updated or a warning if no records were updated. \n ",
    "medium_prompt": "You are creating tests using the Acceptance Test Library that is available for the X++ programming language for Dynamics 365 for Finance And Operations also known as Dynamics AX or Axapta.\n\
\n\
The ATLSpec class is this:\n\
<AtlEntitySMRFUCompaniesTable>\n\
[AtlEntityGenerationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlEntitySMRFUCompaniesTable extends AtlEntity\n\
{\n\
    private SMRFUCompaniesTable sMRFUCompaniesTable;\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable save()\n\
    {\n\
        this.saveBase();\n\
\n\
        return this;\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final Common mainRecordBase()\n\
    {\n\
        return sMRFUCompaniesTable;\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFUCompaniesTable record()\n\
    {\n\
        return this.mainRecordBase();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final void new(boolean _initValue = true)\n\
    {\n\
        if (_initValue)\n\
        {\n\
            sMRFUCompaniesTable.initValue();\n\
        }\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlEntitySMRFUCompaniesTable construct()\n\
    {\n\
        return new AtlEntitySMRFUCompaniesTable();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final void init(SMRFUCompaniesTable _sMRFUCompaniesTable)\n\
    {\n\
        sMRFUCompaniesTable.data(_sMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlEntitySMRFUCompaniesTable newFromRecord(SMRFUCompaniesTable _record)\n\
    {\n\
        AtlEntitySMRFUCompaniesTable entity = new AtlEntitySMRFUCompaniesTable(false);\n\
        entity.init(_record);\n\
        return entity;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFULegalEntityCode parmLegalEntityCode(SMRFULegalEntityCode _legalEntityCode = '')\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode, !prmIsDefault(_legalEntityCode));\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFULegalEntityName parmLegalEntityName(SMRFULegalEntityName _legalEntityName = '')\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName, !prmIsDefault(_legalEntityName));\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFUParentCompany parmParentCompany(SMRFUParentCompany _parentCompany = NoYesCombo::No)\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany, !prmIsDefault(_parentCompany));\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.parmLegalEntityCode(_legalEntityCode);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.setLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.parmLegalEntityName(_legalEntityName);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.parmParentCompany(_parentCompany);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlEntitySMRFUCompaniesTable>\n\
\n\
The ATLSpecification class is:\n\
<AtlSpecSMRFUCompaniesTable>\n\
[AtlSpecGeneratationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlSpecSMRFUCompaniesTable extends AtlSpecification\n\
{\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final TableId expectedRecordTableId()\n\
    {\n\
        return tableNum(SMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlSpecSMRFUCompaniesTable construct()\n\
    {\n\
        return new AtlSpecSMRFUCompaniesTable();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
	protected final Common getRecordByPrimaryKey(anytype _primarykeyValue)\n\
    {\n\
        SMRFUCompaniesTable sMRFUCompaniesTable;\n\
\n\
        select firstonly sMRFUCompaniesTable where sMRFUCompaniesTable.RecId == _primarykeyValue;\n\
\n\
        return sMRFUCompaniesTable;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlSpecSMRFUCompaniesTable, withLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.withLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlSpecSMRFUCompaniesTable> \n\
\n\
The ATL Query class is:\n\
<AtlQuerySMRFUCompaniesTables>\n\
[AtlQueryGenerationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlQuerySMRFUCompaniesTables extends AtlQuery\n\
{\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final TableId baseTableId()\n\
    {\n\
        return tableNum(SMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlQuerySMRFUCompaniesTables construct()\n\
    {\n\
        return new AtlQuerySMRFUCompaniesTables();\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode);\n\
        return this;\n\
    }\n\\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlQuerySMRFUCompaniesTables, withLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.withLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlQuerySMRFUCompaniesTables>\n\
\n\
\n\
Here are some examples of other Test Cases created with the acceptance test library:\n\
<CostingSampleTest>\n\
/// <summary>\n\
/// The <c>CostingSampleTest</c> class contains examples on validating cost and ledger transactions.\n\
/// </summary>\n\
[SysTestCaseDataDependency('USMF')]\n\
[SysTestCaseAutomaticNumberSequences]\n\
public final class CostingSampleTest extends SysTestCase\n\
{\n\
    private const Price                             InitialMaterialPrice = 5.0;\n\
    private const Price                             ChangedMaterialPrice = 6.0;\n\
    private const CostPrice                         InitialCostPrice = 6.65;\n\
    private const CostPrice                         ChangedCostPrice = 7.68;\n\
\n\
    private const InventQty                         OnHandQuantity = 100;\n\
    private const InventQty                         QuantityToProduce = 5;\n\
    private const InventQty                         UpdatedOnHandQuantity = OnHandQuantity - QuantityToProduce;\n\
    private const CostAmount                        MaterialPriceDifference = ChangedMaterialPrice - InitialMaterialPrice;\n\
    private const CostAmount                        PhysicalDirectMaterialPrice = InitialCostPrice * QuantityToProduce;\n\
\n\
    private const CostAmount                        Ovh2Rate = 1.5;\n\
    private const CostAmount                        Ovh3Rate = 0.03;\n\
    private const CostAmount                        InitialMaterialBasis = InitialMaterialPrice * QuantityToProduce; //25\n\
    private const CostAmount                        IndirectCostAmountOVH2 = Ovh2Rate  * QuantityToProduce; //7.5\n\
    private const CostAmount                        InitialCostAmountOVH3 = Ovh3Rate * initialMaterialBasis; //0.75\n\
    private const CostAmount                        ActualPrice = InitialMaterialBasis + IndirectCostAmountOVH2 + InitialCostAmountOVH3;\n\
    private const CostAmount                        ActualPriceVariance = MaterialPriceDifference * QuantityToProduce;\n\
    private const CostAmount                        RevaluationOvh3Basis = ActualPriceVariance;\n\
    private const CostAmount                        RevaluationIndirectCostAmountOVH3 = Ovh3Rate * RevaluationOvh3Basis;\n\
    private const CostAmount                        RevaluationOvh3Delta = InitialCostAmountOVH3 + RevaluationIndirectCostAmountOVH3;\n\
\n\
    private AtlDataRootNode                         data;\n\
    private AtlDataCost                             cost;\n\
    private AtlDataInvent                           invent;\n\
    private AtlDataInventOnHand                     onHand;\n\
    private AtlDataLedger                           ledger;\n\
    private AtlDataProductItems                     items;\n\
    private AtlDataProductionOrders                 productionOrders;\n\
    private AtlDataLedgerMainAccounts               mainAccounts;\n\
    private AtlDataGeneralJournalAccountEntries     accountEntries;\n\
    private AtlDataInventPostings                   postings;\n\
    private AtlDataCostBOMCostGroups                costGroups;\n\
    private AtlDataInventCostTransactions           costTransactions;\n\
    private AtlDataInventCostTransactionVariances   costVariances;\n\
    private AtlDataDimensionAttributeValues         dimensionValues;\n\
    private AtlDataSalesOrders                      salesOrders;\n\
    private AtlDataSalesOrderLines                  salesOrderLines;\n\
    private AtlDataCustPackingSlipJournals          packingSlipJournals;\n\
    private AtlDataCustInvoiceJournals              invoiceJournals;\n\
    private InventSite                              site;\n\
    private InventLocation                          warehouse;\n\
    private InventTable                             item;\n\
    private InventTable                             finishedGood;\n\
    private DimensionAttributeValue                 businessUnit;\n\
    private DimensionAttributeValue                 costCenter;\n\
    private DimensionAttributeValue                 finishedGoodsInventoryAccount;\n\
    private DimensionAttributeValue                 productionWIPMaterialAccount;\n\
    private DimensionAttributeValue                 productionWIPOverheadAccount;\n\
    private DimensionAttributeValue                 productionAbsorbedMachineDepreciationAccount;\n\
    private DimensionAttributeValue                 salesPackingSlipAccount;\n\
    private DimensionAttributeValue                 salesPackingSlipOffsetAccount;\n\
    private DimensionAttributeValue                 salesDeferredRevenueAccount;\n\
    private DimensionAttributeValue                 salesDeferredRevenueOffsetAccount;\n\
    private DimensionAttributeValue                 salesIssueAccount;\n\
    private DimensionAttributeValue                 salesConsumptionAccount;\n\
    private DimensionAttributeValue                 salesRevenueAccount;\n\
    private DimensionAttributeValue                 inventIssueAccount;\n\
    private DimensionAttributeValue                 inventLossAccount;\n\
    private DimensionAttributeValue                 custSummaryAccount;\n\
    private DimensionAttributeValue                 stdCostRevaluationAccount;\n\
    private DimensionAttributeValue                 stdCostChangeVarianceAccount;\n\
    private DimensionAttributeValue                 stdCostRoundingVarianceAccount;\n\
\n\
    private CostingVersionEntity                    costingVersion;\n\
\n\
    public void setUp()\n\
    {\n\
        super();\n\
\n\
        this.initDataSetupReferences();\n\
    }\n\
\n\
    protected void initDataSetupReferences()\n\
    {\n\
        // Create data navigations\n\
        data = AtlDataRootNode::construct();\n\
\n\
        cost = data.cost();\n\
        invent = data.invent();\n\
        onHand = invent.onHand();\n\
        items = invent.items();\n\
        ledger = data.ledger();\n\
        var cust = data.cust();\n\
        var sales = data.sales();\n\
\n\
        mainAccounts = ledger.mainAccounts();\n\
        accountEntries = ledger.generalJournalAccountEntries();\n\
        postings = invent.postings();\n\
        costGroups = cost.bomCostGroups();\n\
        costTransactions = invent.costTransactions();\n\
        costVariances = invent.costTransactionVariances();\n\
        dimensionValues = data.dimensions().values();\n\
        productionOrders = data.prod().productionOrders();\n\
        packingSlipJournals = cust.packingSlipJournals();\n\
        invoiceJournals = cust.invoiceJournals();\n\
        salesOrders = sales.salesOrders();\n\
        salesOrderLines = sales.salesOrderLines();\n\
\n\
        // Create master data\n\
        site = invent.sites().default();                                                    // Create default site\n\
        warehouse = invent.warehouses().default();                                          // Create default warehouse\n\
        item = items.bomStandardCostBuilder().setCostGroup(costGroups.material()).create(); // Create default standard cost item\n\
        costingVersion = data.cost().costingVersions().createDefaultStandard();             // Create default costing version of standard cost items\n\
        var customer = data.cust().customers().default().record();\n\
\n\
        businessUnit = dimensionValues.businessUnits().second();\n\
        costCenter = dimensionValues.costCenters().first();\n\
\n\
        finishedGoodsInventoryAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.finishedGoodsInventory().RecId).first();\n\
        productionWIPMaterialAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionWIPMaterials().RecId).first();\n\
        productionWIPOverheadAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionWIPOverhead().RecId).first();\n\
        productionAbsorbedMachineDepreciationAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionAbsorbedMachineDepreciation().RecId).first();\n\
\n\
        salesPackingSlipAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPackingSlip).firstEntity().mainAccount().record().RecId).first();\n\
        salesPackingSlipOffsetAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPackingSlipOffsetAccount).firstEntity().mainAccount().record().RecId).first();\n\
        salesDeferredRevenueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPckSlipRevenue).firstEntity().mainAccount().record().RecId).first();\n\
        salesDeferredRevenueOffsetAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPckSlipRevenueOffsetAccount).firstEntity().mainAccount().record().RecId).first();\n\
        salesIssueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesIssue).firstEntity().mainAccount().record().RecId).first();\n\
        salesConsumptionAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesConsump).firstEntity().mainAccount().record().RecId).first();\n\
        salesRevenueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesRevenue).firstEntity().mainAccount().record().RecId).first();\n\
        inventIssueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventIssue).firstEntity().mainAccount().record().RecId).first();\n\
        inventLossAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventLoss).firstEntity().mainAccount().record().RecId).first();\n\
\n\
        stdCostRevaluationAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostRevaluation).firstEntity().mainAccount().record().RecId).first();\n\
        stdCostRoundingVarianceAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostRoundingVariance).firstEntity().mainAccount().record().RecId).first();\n\
        stdCostChangeVarianceAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostChangeVariance).firstEntity().mainAccount().record().RecId).first();\n\
\n\
        custSummaryAccount = dimensionValues.mainAccounts().withInstanceRecId(MainAccount::findByLedgerDimension(data.cust().postingProfiles().query().forCustomer(customer).firstEntity().parmSummaryAccountNumber()).RecId).first();\n\
\n\
        // Create finished good item and create BOM\n\
        finishedGood = items.bomStandardCostBuilder().setItemId('stdBOM').setCostGroup(costGroups.composedProduct()).create();\n\
\n\
        var finished = data.products().billsOfMaterials().defaultBuilder().setBOMId(finishedGood.ItemId).setSite(site).save();\n\
        finished.addLine().setItem(item).setQuantity(1).setInventDims([site, warehouse]).save();\n\
        finished.approve().addVersion().setItem(finishedGood).setInventDims([site, warehouse]).save().approveAndActivate();\n\
\n\
        this.setItemPrice(InitialMaterialPrice);\n\
\n\\n\
        // Add on-hand for the item by posting journal\n\
        onHand.adjust().forItem(item).forInventDims([site, warehouse]).setQty(OnHandQuantity).postJournal();\n\
    }\n\
\n\
    /// <summary>\n\
    /// Validates general ledger postings for production order and journals when the cost changes on raw material before ending the production order.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void productionEndingWithMaterialPriceChange()\n\
    {\n\
        var originalDate = DateTimeUtil::getSystemDate(DateTimeUtil::getUserPreferredTimeZone());\n\
        var futureDate = originalDate + 5;\n\
\n\
        // Create production order\n\
        var productionOrder = productionOrders.initDefault()\n\
                                .setItem(finishedGood)\n\
                                .setInventDims([warehouse])\n\
                                .setQuantity(QuantityToProduce)\n\
                                .save();\n\
\n\
        // Estimate, start and report as finish the production order\n\
        productionOrder.estimate().execute();\n\
        productionOrder.start().execute();\n\
        productionOrder.reportAsFinished().execute();\n\
\n\
        // Change the price to ensure that we get price variance\n\
        systemDateSet(futureDate);\n\
        this.setItemPrice(ChangedMaterialPrice);\n\
        systemDateSet(originalDate);\n\
\n\
        // End the production order\n\
        productionOrder.end().execute();\n\
\n\
        // Get calculation voucher\n\
        var calculationVouchers =  productionOrder.indirectCostTransactions().groupByVoucherCalculation();\n\
        calculationVouchers.assertCount(1);\n\
\n\
        var calculationVoucher = calculationVouchers.firstEntity().parmVoucherCalculation();\n\
\n\
        // Get estimation vouchers\n\
        var estimationVouchers =  productionOrder.indirectCostTransactions().groupByVoucherEstimation();\n\
        estimationVouchers.assertCount(4);\n\
\n\
        // Query the Vouchers\n\
        var estimatedRevaluation  = estimationVouchers.firstEntity().parmVoucherEstimation();\n\
        var estimatedVoucherFromCosting  = estimationVouchers.secondEntity().parmVoucherEstimation();\n\
        var estimatedVoucherFromRelease  = estimationVouchers.entityAt(3).parmVoucherEstimation();\n\
        var estimatedVoucherRAF = estimationVouchers.entityAt(4).parmVoucherEstimation();\n\
\n\
        // Validate indirect cost transactions\n\
        productionOrder.indirectCostTransactions().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(-RevaluationIndirectCostAmountOVH3).withBasis(-RevaluationOvh3Basis).withCostGroup(costGroups.materialOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(RevaluationIndirectCostAmountOVH3).withBasis(RevaluationOvh3Basis).withCostGroup(costGroups.materialOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(InitialCostAmountOVH3).withBasis(InitialMaterialBasis).withCostGroup(costGroups.materialOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(InitialCostAmountOVH3).withBasis(InitialMaterialBasis).withCostGroup(costGroups.materialOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(IndirectCostAmountOVH2).withBasis(QuantityToProduce).withCostGroup(costGroups.plantOverhead()).withVoucherCalculation(calculationVoucher).withVoucherEstimation(estimatedVoucherFromCosting))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(IndirectCostAmountOVH2).withBasis(QuantityToProduce).withCostGroup(costGroups.plantOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(-IndirectCostAmountOVH2).withBasis(0).withCostGroup(costGroups.plantOverhead()).withVoucherCalculation(calculationVoucher))\n\
            .addSpec(cost.indirectCostTransactions().spec().withAmount(-InitialCostAmountOVH3).withBasis(0).withCostGroup(costGroups.materialOverhead()).withVoucherCalculation(calculationVoucher))\n\
            , 'Indirect cost transactions');\n\
\n\
        // Validate cost transactions, and related cost variances using the sub specification pattern (withVariances returns a collection of specifications for each of the cost transaction lines)\n\
        costTransactions.query().forItem(item).assertExpectedLinesSet(AtlSpecifications::construct()\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(OnHandQuantity).withWIPInQuantity(0).withWIPOutQuantity(0).withOnHandQuantity(OnHandQuantity))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(0).withWIPOutQuantity(0).withOnHandQuantity(-(UpdatedOnHandQuantity)).withVoucher(estimatedRevaluation))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(UpdatedOnHandQuantity).withWIPInQuantity(0).withWIPOutQuantity(0).withOnHandQuantity(UpdatedOnHandQuantity).withVoucher(estimatedRevaluation)\n\
                   .withVariances(\n\
                        costVariances.spec().withCostGroup(costGroups.material()).withTypeRevaluation().withCostAmountPosted(-UpdatedOnHandQuantity)\n\
                ))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(-QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(0).withVoucher(estimatedRevaluation))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(QuantityToProduce).withWIPInQuantity(QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(0).withVoucher(estimatedRevaluation)\n\
                    .withVariances(\n\
                        costVariances.spec().withCostGroup(costGroups.material()).withTypeRevaluation().withCostAmountPosted(-MaterialPriceDifference * QuantityToProduce)\n\
                ))\n\
                .addSpec(costTransactions.spec().withPhysicalIssue().withVarianceQuantity(0).withWIPInQuantity(QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(-QuantityToProduce).withVoucher(estimatedVoucherFromRelease))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVoucher(calculationVoucher).withVarianceQuantity(-QuantityToProduce).withWIPInQuantity(-QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting)\n\
                    .withVariances(\n\
                        costVariances.spec().withCostGroup(costGroups.material()).withTypeRevaluation().withCostAmountPosted(MaterialPriceDifference * QuantityToProduce)\n\
                ))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(-QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(QuantityToProduce).withWIPOutQuantity(0).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting))\n\
            , 'Cost transactions for RAW material');\n\
\n\
        // Validate cost transaction for the finished good\n\
        costTransactions.query().forItem(finishedGood).assertExpectedLinesSet(AtlSpecifications::construct()\n\
                .addSpec(costTransactions.spec().withPhysicalReceipt().withVarianceQuantity(QuantityToProduce).withWIPInQuantity(0).withWIPOutQuantity(-QuantityToProduce).withOnHandQuantity(QuantityToProduce).withVoucher(estimatedVoucherRAF))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(QuantityToProduce).withWIPInQuantity(0).withWIPOutQuantity(QuantityToProduce).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(QuantityToProduce).withWIPInQuantity(0).withWIPOutQuantity(QuantityToProduce).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(0).withWIPOutQuantity(-QuantityToProduce).withOnHandQuantity(0).withVoucher(estimatedVoucherFromCosting))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(QuantityToProduce).withWIPInQuantity(0).withWIPOutQuantity(0).withOnHandQuantity(QuantityToProduce))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(0).withWIPOutQuantity(0).withOnHandQuantity(-QuantityToProduce))\n\
                .addSpec(costTransactions.spec().withFinancialReceipt().withVarianceQuantity(-QuantityToProduce).withWIPInQuantity(0).withWIPOutQuantity(-QuantityToProduce).withOnHandQuantity(0))\n\
                .addSpec(costTransactions.spec().withFinancialIssue().withVarianceQuantity(0).withWIPInQuantity(0).withWIPOutQuantity(QuantityToProduce).withOnHandQuantity(0))\n\
            , 'Cost transactions for Finished Good');\n\
\n\
        // Validate journal account entries amounts and related main accounts\n\
        productionOrder.postings().withJournalTypeCosting().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(data.prod().postings().spec().withQuantityGood(QuantityToProduce).withAmountFinancial(ActualPrice)\n\
                .withJournalAccountEntries(AtlSpecifications::construct()\n\
                    .addSpec(accountEntries.spec().withAmount(IndirectCostAmountOVH2 + InitialCostAmountOVH3))\n\
                    .addSpec(accountEntries.spec().withAmount(InitialMaterialBasis))\n\
                    .addSpec(accountEntries.spec().withAmount(-ActualPrice))\n\
                    .addSpec(accountEntries.spec().withAmount(-InitialCostAmountOVH3).forMainAccount(mainAccounts.productionAbsorbedInternalLogistics()))\n\
                    .addSpec(accountEntries.spec().withAmount(round(RevaluationOvh3Delta, 0.01)).forMainAccount(mainAccounts.productionAbsorbedInternalLogistics()))\n\
                    .addSpec(accountEntries.spec().withAmount(-(IndirectCostAmountOVH2 + round(RevaluationOvh3Delta,0.01))).forMainAccount(mainAccounts.productionWIPOverhead()))\n\
                    .addSpec(accountEntries.spec().withAmount(PhysicalDirectMaterialPrice).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(-PhysicalDirectMaterialPrice).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(InitialMaterialBasis).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(-InitialMaterialBasis).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(-InitialMaterialBasis).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPrice).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withAmount(-IndirectCostAmountOVH2).forMainAccount(mainAccounts.productionAbsorbedMachineDepreciation()))\n\
                    .addSpec(accountEntries.spec().withAmount(IndirectCostAmountOVH2).forMainAccount(mainAccounts.productionAbsorbedMachineDepreciation()))\n\
                    .addSpec(accountEntries.spec().withAmount(round(RevaluationIndirectCostAmountOVH3, 0.01)).forMainAccount(mainAccounts.productionAbsorbedInternalLogistics()))\n\
                    .addSpec(accountEntries.spec().withAmount(-round(RevaluationIndirectCostAmountOVH3, 0.01)).forMainAccount(mainAccounts.productionWIPOverhead()))\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPriceVariance).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(-ActualPriceVariance).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPriceVariance+RevaluationIndirectCostAmountOVH3).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(-(ActualPriceVariance+RevaluationIndirectCostAmountOVH3)).forMainAccount(mainAccounts.finishedGoodsInventory()))\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPriceVariance+RevaluationIndirectCostAmountOVH3).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withAmount(-ActualPriceVariance).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withAmount(-RevaluationIndirectCostAmountOVH3))\n\
                ))\n\
            , 'Postings for costing');\n\
\n\
        // Validate main account using dimensions attributes\n\
        productionOrder.postings().withJournalTypeReportAsFinished().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(data.prod().postings().spec().withAmountPhysical(ActualPrice).withQuantityGood(QuantityToProduce)\n\
                .withJournalAccountEntries(AtlSpecifications::construct()\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPrice).withDimensionAttributeValues([finishedGoodsInventoryAccount]))\n\
                    .addSpec(accountEntries.spec().withAmount(-ActualPrice).withDimensionAttributeValues([productionWIPMaterialAccount]))\n\
                    .addSpec(accountEntries.spec().withAmount(IndirectCostAmountOVH2).withDimensionAttributeValues([productionWIPOverheadAccount]))\n\
                    .addSpec(accountEntries.spec().withAmount(-IndirectCostAmountOVH2).withDimensionAttributeValues([productionAbsorbedMachineDepreciationAccount]))\n\
                ))\n\
            , 'Postings for report as finished');\
\n\
        // Validate postings using a mix of main accounts (forMainAccount) and dimensions attributes (withDimensionAttributeValues)\n\
        productionOrder.postings().withJournalTypeRelease().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(data.prod().postings().spec().withAmountPhysical(InitialMaterialBasis).withQuantityGood(0)\n\
                .withJournalAccountEntries(AtlSpecifications::construct()\n\
                    .addSpec(accountEntries.spec().withAmount(InitialMaterialBasis).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withDimensionAttributeValues([finishedGoodsInventoryAccount]).withAmount(-InitialMaterialBasis))\n\
                    .addSpec(accountEntries.spec().withAmount(InitialCostAmountOVH3).forMainAccount(mainAccounts.productionWIPOverhead()))\n\
                    .addSpec(accountEntries.spec().withAmount(-InitialCostAmountOVH3).forMainAccount(mainAccounts.productionAbsorbedInternalLogistics()))))\n\
            .addSpec(data.prod().postings().spec().withAmountPhysical(ActualPriceVariance).withQuantityGood(0)\n\
                .withJournalAccountEntries(AtlSpecifications::construct()\n\
                    .addSpec(accountEntries.spec().withAmount(ActualPriceVariance).forMainAccount(mainAccounts.productionWIPMaterials()))\n\
                    .addSpec(accountEntries.spec().withDimensionAttributeValues([finishedGoodsInventoryAccount]).withAmount(-ActualPriceVariance))\n\
                    .addSpec(accountEntries.spec().withAmount(round(-RevaluationIndirectCostAmountOVH3, 0.01)).forMainAccount(mainAccounts.productionAbsorbedInternalLogistics()))\n\
                    .addSpec(accountEntries.spec().withAmount(round(RevaluationIndirectCostAmountOVH3, 0.01)).forMainAccount(mainAccounts.productionWIPOverhead()))\n\
                    .addSpec(accountEntries.spec().withDimensionAttributeValues([finishedGoodsInventoryAccount]).withAmount(MaterialPriceDifference * OnHandQuantity))\n\
                    .addSpec(accountEntries.spec().withAmount(-MaterialPriceDifference * OnHandQuantity).forMainAccount(mainAccounts.inventoryCostRevaluation()))))\n\
            .addSpec(data.prod().postings().spec().withAmountPhysical(-ActualPriceVariance).withQuantityGood(0))\n\
            , 'Postings for material consumption');\n\
    }\n\
\n\
    /// <summary>\n\
    /// Validates general ledger postings for sales order with partial packing slip and cost price is changed between posting of two invoices.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void salesPartialPackingAndInvoice()\n\
    {\n\
        const SalesPrice    UnitPrice = 12;\n\
        const SalesQty      SalesQuantity = 10;\n\
        const SalesQty      PackingSlipQuantity = 5;\n\
        const SalesQty      FirstInvoiceQuantity = 3;\n\
        const SalesQty      SecondInvoiceQuantity = 7;\n\
        const SalesQty      DeltaPackingAndInvoice = PackingSlipQuantity - FirstInvoiceQuantity;\n\
\n\
        // Create sales order and line\n\
        var salesOrder = salesorders.initDefault().setDefaultDimensions([businessUnit]).save();\n\
        var salesOrderLine = salesOrder.addLine().setItem(item).setQuantity(SalesQuantity).setInventDims([warehouse]).setPrice(UnitPrice).setDeliverNow(PackingSlipQuantity).setDefaultDimensions([businessUnit, costCenter]).save();\n\
\n\
        // Validate default dimensions on sales order and line\n\
        salesOrders.query().withSalesId(salesOrder.parmSalesId()).assertExpectedLines(salesorders.spec().withDefaultDimensions([businessUnit]));\n\
        salesOrderLines.query().forSalesOrder(salesOrder).assertExpectedLines(salesOrderLines.spec().withDefaultDimensions([businessUnit, costCenter]));\n\
\n\
        // Post packing slip with deliver now quantity\n\
        salesOrder.postPackingSlip(SalesUpdate::DeliverNow);\n\
\n\
        // Set delivery now for invoice quantity\n\
        salesOrder.lines().firstEntity().setDeliverNow(FirstInvoiceQuantity).save();\n\
\n\
        // Post first invoice for delivery now quantity\n\
        salesOrder.postInvoice(SalesUpdate::DeliverNow);\n\
\n\
        // Change the price\n\
        this.setItemPrice(ChangedMaterialPrice);\n\
\n\
        // Post second invoice for remaining quantity\n\
        salesOrder.postInvoice(SalesUpdate::All);\n\
\n\
        // Validate account entries for packing slip using dimensions attributes\n\
        var firstPackingSlip = salesOrder.packingSlipJournals().firstEntity();\n\
        firstPackingSlip.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * PackingSlipQuantity).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * PackingSlipQuantity).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * PackingSlipQuantity).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * PackingSlipQuantity).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            , 'Account entries on sales packing slip');\n\
\n\
        var packingSlipVersions = firstPackingSlip.versions();\n\
\n\
        this.assertEquals(1, packingSlipVersions.count(), 'Expected one packing slip posted');\n\
\n\
        var invoices = salesOrder.invoices().orderByInvoiceNumber(SortOrder::Ascending);\n\
\n\
        // Validate account entries for first invoice using dimensions attributes\n\
        var firstInvoice = invoices.firstEntity();\n\
        firstInvoice.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesIssueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesIssue))\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesConsumptionAccount, businessUnit]).withPostingType(LedgerPostingType::SalesConsump))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([custSummaryAccount, businessUnit]).withPostingType(LedgerPostingType::CustBalance))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesRevenue))\n\
            , 'Account entries on first sales invoice');\n\
\n\
        // Validate account entries for second invoice using dimensions attributes\n\
        var secondInvoice = invoices.secondEntity();\n\
        secondInvoice.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount( ChangedMaterialPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-ChangedMaterialPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-ChangedMaterialPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesIssueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesIssue))\n\
            .addSpec(accountEntries.spec().withAmount( ChangedMaterialPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesConsumptionAccount, businessUnit]).withPostingType(LedgerPostingType::SalesConsump))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * SecondInvoiceQuantity).withDimensionAttributeValues([custSummaryAccount, businessUnit]).withPostingType(LedgerPostingType::CustBalance))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesRevenue))\n\
            , 'Account entries on second sales invoice');\n\
\n\
        // Query active cost prices and get the initial and changed cost prices based on ordering by activation of the cost prices\n\
        var prices = invent.prices().queryActive().forInventTable(item).withPriceTypeCostPrice().orderByActivation();\n\
        var changedPrice = prices.firstEntity();\n\
        var initialPrice = prices.secondEntity();\n\
\n\
        // Validate cost transactions for item\n\
        costTransactions.query().forItem(item).assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(0).withVarianceQuantity(OnHandQuantity).withOnHandQuantity(OnHandQuantity)\n\
                                            .withFinancialReceipt().forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(DeltaPackingAndInvoice).withVarianceQuantity(OnHandQuantity-FirstInvoiceQuantity).withOnHandQuantity(OnHandQuantity-PackingSlipQuantity)\n\
                                            .withFinancialReceipt().withVoucher(changedPrice.parmStdCostVoucher()).forPrice(changedPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(-DeltaPackingAndInvoice).withVarianceQuantity(0).withOnHandQuantity(-(OnHandQuantity-PackingSlipQuantity))\n\
                                            .withFinancialIssue().withVoucher(changedPrice.parmStdCostVoucher()).forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(FirstInvoiceQuantity).withDeferredCogsQuantity(-FirstInvoiceQuantity).withVarianceQuantity(0).withOnHandQuantity(0)\n\
                                            .withFinancialIssue().withVoucher(firstInvoice.parmLedgerVoucherNumber()).forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(SecondInvoiceQuantity).withDeferredCogsQuantity(-DeltaPackingAndInvoice).withVarianceQuantity(0).withOnHandQuantity(-(SalesQuantity-PackingSlipQuantity))\n\
                                            .withFinancialIssue().withVoucher(secondInvoice.parmLedgerVoucherNumber()).forPrice(changedPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(PackingSlipQuantity).withVarianceQuantity(0).withOnHandQuantity(-PackingSlipQuantity)\n\
                                            .withPhysicalIssue().withVoucher(firstPackingSlip.parmLedgerVoucherNumber()).forPrice(initialPrice))\n\
            , 'Cost transactions for item');\n\
    }\n\
\n\
    private void setItemPrice(Price _price)\n\
    {\n\
        // Create and activate a standard cost price\n\
        invent.prices().initCostPrice()\n\
            .setVersion(costingVersion)     // Using the default costing version\n\
            .setItem(item)                  // For the default standard cost item\n\
            .setPrice(_price)               // With a given cost price\n\
            .save()                         // Save the item cost price\n\
            .activate();                    // Activate the item cost price\n\
\n\
        // Calculate standard cost price for the finished good based on the BOM\n\
        costingVersion.calculate().setItem(finishedGood).setQuantity(1).setProcurementMode(ItemProcurementMode::ProductionOrder).execute();\n\
    }\n\
\n\
}\n\
</CostingSampleTest>\n\
\n\
Your explicit instructions are:\n\
1. Look at the Specification, Entity and Query classes I gave you.\n\
2. Look at the example of a test made with the acceptance test library.\n\
3. Create tests covering all test cases based on the example and using the specification, entity and query classs.\n\
\n\
Only return the test class, no additional information is necessary.\n\
",














    "large_prompt": "Here is the extended system_prompt for code generation in X++ using the Acceptance Test Library:\n\
You are creating tests using the Acceptance Test Library that is available for the X++ programming language for Dynamics 365 for Finance And Operations also known as Dynamics AX or Axapta.\n\
The Acceptance Test Library in X++ provides a framework for writing automated acceptance tests. It allows you to define test cases, execute them, and validate the results. The library provides classes and methods to interact with the application, perform actions, and make assertions.\n\
When creating tests using the Acceptance Test Library, follow these guidelines:\n\
\n\
Organize your tests into test suites and test cases. Use the SysTestSuite class to define test suites and the SysTestCase class to define individual test cases.\n\
Use the provided classes and methods from the Acceptance Test Library to interact with the application. For example, use the SysTestEntityController class to perform CRUD operations on entities, and the SysTestQuery class to execute queries and validate results.\n\
Make use of the Specification, Entity, and Query classes provided to you. These classes define the business logic, data model, and query capabilities of the application. Utilize them to set up test data, execute business processes, and validate the expected outcomes.\n\
Follow the example of the test made with the Acceptance Test Library. Use it as a reference to structure your tests, handle test data, and make assertions.\n\
Ensure that your tests cover all the relevant test cases based on the provided Specification, Entity, and Query classes. Consider different scenarios, edge cases, and possible exceptions.\n\
Use meaningful names for your test suites, test cases, and variables to enhance readability and maintainability of your test code.\n\
Utilize the assertion methods provided by the Acceptance Test Library to validate the expected results. Use methods like assertEquals, assertNotNull, assertTrue, etc., to compare the actual results with the expected outcomes.\n\
Handle exceptions and errors gracefully in your tests. Use try-catch blocks to catch and handle expected exceptions, and use the assertFail method to fail the test if an unexpected exception occurs."
                    "Here are the necessary classes:"
                    "The ATLSpec class is this:\n\
<AtlEntitySMRFUCompaniesTable>\n\
[AtlEntityGenerationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlEntitySMRFUCompaniesTable extends AtlEntity\n\
{\n\
    private SMRFUCompaniesTable sMRFUCompaniesTable;\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable save()\n\
    {\n\
        this.saveBase();\n\
\n\
        return this;\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final Common mainRecordBase()\n\
    {\n\
        return sMRFUCompaniesTable;\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFUCompaniesTable record()\n\
    {\n\
        return this.mainRecordBase();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final void new(boolean _initValue = true)\n\
    {\n\
        if (_initValue)\n\
        {\n\
            sMRFUCompaniesTable.initValue();\n\
        }\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlEntitySMRFUCompaniesTable construct()\n\
    {\n\
        return new AtlEntitySMRFUCompaniesTable();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final void init(SMRFUCompaniesTable _sMRFUCompaniesTable)\n\
    {\n\
        sMRFUCompaniesTable.data(_sMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlEntitySMRFUCompaniesTable newFromRecord(SMRFUCompaniesTable _record)\n\
    {\n\
        AtlEntitySMRFUCompaniesTable entity = new AtlEntitySMRFUCompaniesTable(false);\n\
        entity.init(_record);\n\
        return entity;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFULegalEntityCode parmLegalEntityCode(SMRFULegalEntityCode _legalEntityCode = '')\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode, !prmIsDefault(_legalEntityCode));\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFULegalEntityName parmLegalEntityName(SMRFULegalEntityName _legalEntityName = '')\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName, !prmIsDefault(_legalEntityName));\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final SMRFUParentCompany parmParentCompany(SMRFUParentCompany _parentCompany = NoYesCombo::No)\n\
    {\n\
        return this.parmMainRecordField(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany, !prmIsDefault(_parentCompany));\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.parmLegalEntityCode(_legalEntityCode);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.setLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmLegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.parmLegalEntityName(_legalEntityName);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlEntitySMRFUCompaniesTable, parmParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlEntitySMRFUCompaniesTable setParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.parmParentCompany(_parentCompany);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlEntitySMRFUCompaniesTable>\n\
\n\
The ATLSpecification class is:\n\
<AtlSpecSMRFUCompaniesTable>\n\
[AtlSpecGeneratationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlSpecSMRFUCompaniesTable extends AtlSpecification\n\
{\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final TableId expectedRecordTableId()\n\
    {\n\
        return tableNum(SMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlSpecSMRFUCompaniesTable construct()\n\
    {\n\
        return new AtlSpecSMRFUCompaniesTable();\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
	protected final Common getRecordByPrimaryKey(anytype _primarykeyValue)\n\
    {\n\
        SMRFUCompaniesTable sMRFUCompaniesTable;\n\
\n\
        select firstonly sMRFUCompaniesTable where sMRFUCompaniesTable.RecId == _primarykeyValue;\n\
\n\
        return sMRFUCompaniesTable;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlSpecSMRFUCompaniesTable, withLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.withLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlSpecSMRFUCompaniesTable withParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.parmExpectedFieldValue(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlSpecSMRFUCompaniesTable> \n\
\n\
The ATL Query class is:\n\
<AtlQuerySMRFUCompaniesTables>\n\
[AtlQueryGenerationDependentTable(tableStr(SMRFUCompaniesTable))]\n\
public final class AtlQuerySMRFUCompaniesTables extends AtlQuery\n\
{\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0')]\n\
    protected final TableId baseTableId()\n\
    {\n\
        return tableNum(SMRFUCompaniesTable);\n\
    }\n\
\n\
    [SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public static AtlQuerySMRFUCompaniesTables construct()\n\
    {\n\
        return new AtlQuerySMRFUCompaniesTables();\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntityCode(SMRFULegalEntityCode _legalEntityCode)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, LegalEntityCode), _legalEntityCode);\n\
        return this;\n\
    }\n\\n\
\n\
    [AtlDependentFluentSetter(methodStr(AtlQuerySMRFUCompaniesTables, withLegalEntityCode)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntity(CompanyInfo _companyInfo)\n\
    {\n\
        return this.withLegalEntityCode(_companyInfo.DataArea);\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, ParentCompany)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withParentCompany(SMRFUParentCompany _parentCompany)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, ParentCompany), _parentCompany);\n\
        return this;\n\
    }\n\
\n\
    [AtlDependentField(fieldStr(SMRFUCompaniesTable, LegalEntityName)), SysGeneratedCode('AtlGenerator', '1.0.0.0'), Hookable(false)]\n\
    public final AtlQuerySMRFUCompaniesTables withLegalEntityName(SMRFULegalEntityName _legalEntityName)\n\
    {\n\
        this.addQueryRange(fieldNum(SMRFUCompaniesTable, LegalEntityName), _legalEntityName);\n\
        return this;\n\
    }\n\
\n\
}\n\
</AtlQuerySMRFUCompaniesTables>\n\
\n\
\n"
                    "Here are some examples of other Test Cases created with the acceptance test library:\n\
<CostingSampleTest>\n\
/// <summary>\n\
/// The <c>CostingSampleTest</c> class contains examples on validating cost and ledger transactions.\n\
/// </summary>\n\
[SysTestCaseDataDependency('USMF')]\n\
[SysTestCaseAutomaticNumberSequences]\n\
public final class CostingSampleTest extends SysTestCase\n\
{\n\
    private const Price                             InitialMaterialPrice = 5.0;\n\
    private const Price                             ChangedMaterialPrice = 6.0;\n\
    private const CostPrice                         InitialCostPrice = 6.65;\n\
    private const CostPrice                         ChangedCostPrice = 7.68;\n\
\n\
    private const InventQty                         OnHandQuantity = 100;\n\
    private const InventQty                         QuantityToProduce = 5;\n\
    private const InventQty                         UpdatedOnHandQuantity = OnHandQuantity - QuantityToProduce;\n\
    private const CostAmount                        MaterialPriceDifference = ChangedMaterialPrice - InitialMaterialPrice;\n\
    private const CostAmount                        PhysicalDirectMaterialPrice = InitialCostPrice * QuantityToProduce;\n\
\n\
    private const CostAmount                        Ovh2Rate = 1.5;\n\
    private const CostAmount                        Ovh3Rate = 0.03;\n\
    private const CostAmount                        InitialMaterialBasis = InitialMaterialPrice * QuantityToProduce; //25\n\
    private const CostAmount                        IndirectCostAmountOVH2 = Ovh2Rate  * QuantityToProduce; //7.5\n\
    private const CostAmount                        InitialCostAmountOVH3 = Ovh3Rate * initialMaterialBasis; //0.75\n\
    private const CostAmount                        ActualPrice = InitialMaterialBasis + IndirectCostAmountOVH2 + InitialCostAmountOVH3;\n\
    private const CostAmount                        ActualPriceVariance = MaterialPriceDifference * QuantityToProduce;\n\
    private const CostAmount                        RevaluationOvh3Basis = ActualPriceVariance;\n\
    private const CostAmount                        RevaluationIndirectCostAmountOVH3 = Ovh3Rate * RevaluationOvh3Basis;\n\
    private const CostAmount                        RevaluationOvh3Delta = InitialCostAmountOVH3 + RevaluationIndirectCostAmountOVH3;\n\
\n\
    private AtlDataRootNode                         data;\n\
    private AtlDataCost                             cost;\n\
    private AtlDataInvent                           invent;\n\
    private AtlDataInventOnHand                     onHand;\n\
    private AtlDataLedger                           ledger;\n\
    private AtlDataProductItems                     items;\n\
    private AtlDataProductionOrders                 productionOrders;\n\
    private AtlDataLedgerMainAccounts               mainAccounts;\n\
    private AtlDataGeneralJournalAccountEntries     accountEntries;\n\
    private AtlDataInventPostings                   postings;\n\
    private AtlDataCostBOMCostGroups                costGroups;\n\
    private AtlDataInventCostTransactions           costTransactions;\n\
    private AtlDataInventCostTransactionVariances   costVariances;\n\
    private AtlDataDimensionAttributeValues         dimensionValues;\n\
    private AtlDataSalesOrders                      salesOrders;\n\
    private AtlDataSalesOrderLines                  salesOrderLines;\n\
    private AtlDataCustPackingSlipJournals          packingSlipJournals;\n\
    private AtlDataCustInvoiceJournals              invoiceJournals;\n\
    private InventSite                              site;\n\
    private InventLocation                          warehouse;\n\
    private InventTable                             item;\n\
    private InventTable                             finishedGood;\n\
    private DimensionAttributeValue                 businessUnit;\n\
    private DimensionAttributeValue                 costCenter;\n\
    private DimensionAttributeValue                 finishedGoodsInventoryAccount;\n\
    private DimensionAttributeValue                 productionWIPMaterialAccount;\n\
    private DimensionAttributeValue                 productionWIPOverheadAccount;\n\
    private DimensionAttributeValue                 productionAbsorbedMachineDepreciationAccount;\n\
    private DimensionAttributeValue                 salesPackingSlipAccount;\n\
    private DimensionAttributeValue                 salesPackingSlipOffsetAccount;\n\
    private DimensionAttributeValue                 salesDeferredRevenueAccount;\n\
    private DimensionAttributeValue                 salesDeferredRevenueOffsetAccount;\n\
    private DimensionAttributeValue                 salesIssueAccount;\n\
    private DimensionAttributeValue                 salesConsumptionAccount;\n\
    private DimensionAttributeValue                 salesRevenueAccount;\n\
    private DimensionAttributeValue                 inventIssueAccount;\n\
    private DimensionAttributeValue                 inventLossAccount;\n\
    private DimensionAttributeValue                 custSummaryAccount;\n\
    private DimensionAttributeValue                 stdCostRevaluationAccount;\n\
    private DimensionAttributeValue                 stdCostChangeVarianceAccount;\n\
    private DimensionAttributeValue                 stdCostRoundingVarianceAccount;\n\
\n\
    private CostingVersionEntity                    costingVersion;\n\
\n\
    public void setUp()\n\
    {\n\
        super();\n\
\n\
        this.initDataSetupReferences();\n\
    }\n\
\n\
    protected void initDataSetupReferences()\n\
    {\n\
        // Create data navigations\n\
        data = AtlDataRootNode::construct();\n\
\n\
        cost = data.cost();\n\
        invent = data.invent();\n\
        onHand = invent.onHand();\n\
        items = invent.items();\n\
        ledger = data.ledger();\n\
        var cust = data.cust();\n\
        var sales = data.sales();\n\
\n\
        mainAccounts = ledger.mainAccounts();\n\
        accountEntries = ledger.generalJournalAccountEntries();\n\
        postings = invent.postings();\n\
        costGroups = cost.bomCostGroups();\n\
        costTransactions = invent.costTransactions();\n\
        costVariances = invent.costTransactionVariances();\n\
        dimensionValues = data.dimensions().values();\n\
        productionOrders = data.prod().productionOrders();\n\
        packingSlipJournals = cust.packingSlipJournals();\n\
        invoiceJournals = cust.invoiceJournals();\n\
        salesOrders = sales.salesOrders();\n\
        salesOrderLines = sales.salesOrderLines();\n\
\n\
        // Create master data\n\
        site = invent.sites().default();                                                    // Create default site\n\
        warehouse = invent.warehouses().default();                                          // Create default warehouse\n\
        item = items.bomStandardCostBuilder().setCostGroup(costGroups.material()).create(); // Create default standard cost item\n\
        costingVersion = data.cost().costingVersions().createDefaultStandard();             // Create default costing version of standard cost items\n\
        var customer = data.cust().customers().default().record();\n\
\n\
        businessUnit = dimensionValues.businessUnits().second();\n\
        costCenter = dimensionValues.costCenters().first();\n\
\n\
        finishedGoodsInventoryAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.finishedGoodsInventory().RecId).first();\n\
        productionWIPMaterialAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionWIPMaterials().RecId).first();\n\
        productionWIPOverheadAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionWIPOverhead().RecId).first();\n\
        productionAbsorbedMachineDepreciationAccount = dimensionValues.mainAccounts().withInstanceRecId(mainAccounts.productionAbsorbedMachineDepreciation().RecId).first();\n\
\n\
        salesPackingSlipAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPackingSlip).firstEntity().mainAccount().record().RecId).first();\n\
        salesPackingSlipOffsetAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPackingSlipOffsetAccount).firstEntity().mainAccount().record().RecId).first();\n\
        salesDeferredRevenueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPckSlipRevenue).firstEntity().mainAccount().record().RecId).first();\n\
        salesDeferredRevenueOffsetAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesPckSlipRevenueOffsetAccount).firstEntity().mainAccount().record().RecId).first();\n\
        salesIssueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesIssue).firstEntity().mainAccount().record().RecId).first();\n\
        salesConsumptionAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesConsump).firstEntity().mainAccount().record().RecId).first();\n\
        salesRevenueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::SalesRevenue).firstEntity().mainAccount().record().RecId).first();\n\
        inventIssueAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventIssue).firstEntity().mainAccount().record().RecId).first();\n\
        inventLossAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventLoss).firstEntity().mainAccount().record().RecId).first();\n\
\n\
        stdCostRevaluationAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostRevaluation).firstEntity().mainAccount().record().RecId).first();\n\
        stdCostRoundingVarianceAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostRoundingVariance).firstEntity().mainAccount().record().RecId).first();\n\
        stdCostChangeVarianceAccount = dimensionValues.mainAccounts().withInstanceRecId(data.invent().postings().query().forItem(item).forCustomer(customer).withType(InventAccountType::InventStdCostChangeVariance).firstEntity().mainAccount().record().RecId).first();\n\
\n\
        custSummaryAccount = dimensionValues.mainAccounts().withInstanceRecId(MainAccount::findByLedgerDimension(data.cust().postingProfiles().query().forCustomer(customer).firstEntity().parmSummaryAccountNumber()).RecId).first();\n\
\n\
        // Create finished good item and create BOM\n\
        finishedGood = items.bomStandardCostBuilder().setItemId('stdBOM').setCostGroup(costGroups.composedProduct()).create();\n\
\n\
        var finished = data.products().billsOfMaterials().defaultBuilder().setBOMId(finishedGood.ItemId).setSite(site).save();\n\
        finished.addLine().setItem(item).setQuantity(1).setInventDims([site, warehouse]).save();\n\
        finished.approve().addVersion().setItem(finishedGood).setInventDims([site, warehouse]).save().approveAndActivate();\n\
\n\
        this.setItemPrice(InitialMaterialPrice);\n\
\n\\n\
        // Add on-hand for the item by posting journal\n\
        onHand.adjust().forItem(item).forInventDims([site, warehouse]).setQty(OnHandQuantity).postJournal();\n\
    }\n\
\n\
    /// <summary>\n\
    /// Validates general ledger postings for production order and journals when the cost changes on raw material before ending the production order.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void productionEndingWithMaterialPriceChange()\n\
    {\n\
        var originalDate = DateTimeUtil::getSystemDate(DateTimeUtil::getUserPreferredTimeZone());\n\
        var futureDate = originalDate + 5;\n\
\n\
        // Create production order\n\
        var productionOrder = productionOrders.initDefault()\n\
                                .setItem(finishedGood)\n\
                                .setInventDims([warehouse])\n\
                                .setQuantity(QuantityToProduce)\n\
                                .save();\n\
                                    /// <summary>\n\
    /// Validates general ledger postings for sales order with partial packing slip and cost price is changed between posting of two invoices.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void salesPartialPackingAndInvoice()\n\
    {\n\
        const SalesPrice    UnitPrice = 12;\n\
        const SalesQty      SalesQuantity = 10;\n\
        const SalesQty      PackingSlipQuantity = 5;\n\
        const SalesQty      FirstInvoiceQuantity = 3;\n\
        const SalesQty      SecondInvoiceQuantity = 7;\n\
        const SalesQty      DeltaPackingAndInvoice = PackingSlipQuantity - FirstInvoiceQuantity;\n\
\n\
        // Create sales order and line\n\
        var salesOrder = salesorders.initDefault().setDefaultDimensions([businessUnit]).save();\n\
        var salesOrderLine = salesOrder.addLine().setItem(item).setQuantity(SalesQuantity).setInventDims([warehouse]).setPrice(UnitPrice).setDeliverNow(PackingSlipQuantity).setDefaultDimensions([businessUnit, costCenter]).save();\n\
\n\
        // Validate default dimensions on sales order and line\n\
        salesOrders.query().withSalesId(salesOrder.parmSalesId()).assertExpectedLines(salesorders.spec().withDefaultDimensions([businessUnit]));\n\
        salesOrderLines.query().forSalesOrder(salesOrder).assertExpectedLines(salesOrderLines.spec().withDefaultDimensions([businessUnit, costCenter]));\n\
\n\
        // Post packing slip with deliver now quantity\n\
        salesOrder.postPackingSlip(SalesUpdate::DeliverNow);\n\
\n\
        // Set delivery now for invoice quantity\n\
        salesOrder.lines().firstEntity().setDeliverNow(FirstInvoiceQuantity).save();\n\
\n\
        // Post first invoice for delivery now quantity\n\
        salesOrder.postInvoice(SalesUpdate::DeliverNow);\n\
\n\
        // Change the price\n\
        this.setItemPrice(ChangedMaterialPrice);\n\
\n\
        // Post second invoice for remaining quantity\n\
        salesOrder.postInvoice(SalesUpdate::All);\n\
\n\
        // Validate account entries for packing slip using dimensions attributes\n\
        var firstPackingSlip = salesOrder.packingSlipJournals().firstEntity();\n\
        firstPackingSlip.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * PackingSlipQuantity).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * PackingSlipQuantity).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * PackingSlipQuantity).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * PackingSlipQuantity).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            , 'Account entries on sales packing slip');\n\
\n\
        var packingSlipVersions = firstPackingSlip.versions();\n\
\n\
        this.assertEquals(1, packingSlipVersions.count(), 'Expected one packing slip posted');\n\
\n\
        var invoices = salesOrder.invoices().orderByInvoiceNumber(SortOrder::Ascending);\n\
\n\
        // Validate account entries for first invoice using dimensions attributes\n\
        var firstInvoice = invoices.firstEntity();\n\
        firstInvoice.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesIssueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesIssue))\n\
            .addSpec(accountEntries.spec().withAmount( InitialMaterialPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesConsumptionAccount, businessUnit]).withPostingType(LedgerPostingType::SalesConsump))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([custSummaryAccount, businessUnit]).withPostingType(LedgerPostingType::CustBalance))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * FirstInvoiceQuantity).withDimensionAttributeValues([salesRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesRevenue))\n\
            , 'Account entries on first sales invoice');\n\
\n\
        // Validate account entries for second invoice using dimensions attributes\n\
        var secondInvoice = invoices.secondEntity();\n\
        secondInvoice.voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount( ChangedMaterialPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesPackingSlipAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-ChangedMaterialPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesPackingSlipOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesOffsetAccountPackingSlip))\n\
            .addSpec(accountEntries.spec().withAmount(-ChangedMaterialPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesIssueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesIssue))\n\
            .addSpec(accountEntries.spec().withAmount( ChangedMaterialPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesConsumptionAccount, businessUnit]).withPostingType(LedgerPostingType::SalesConsump))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesDeferredRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenue))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * DeltaPackingAndInvoice).withDimensionAttributeValues([salesDeferredRevenueOffsetAccount, businessUnit]).withPostingType(LedgerPostingType::SalesPckSlipRevenueOffsetAccount))\n\
            .addSpec(accountEntries.spec().withAmount( UnitPrice * SecondInvoiceQuantity).withDimensionAttributeValues([custSummaryAccount, businessUnit]).withPostingType(LedgerPostingType::CustBalance))\n\
            .addSpec(accountEntries.spec().withAmount(-UnitPrice * SecondInvoiceQuantity).withDimensionAttributeValues([salesRevenueAccount, businessUnit]).withPostingType(LedgerPostingType::SalesRevenue))\n\
            , 'Account entries on second sales invoice');\n\
\n\
        // Query active cost prices and get the initial and changed cost prices based on ordering by activation of the cost prices\n\
        var prices = invent.prices().queryActive().forInventTable(item).withPriceTypeCostPrice().orderByActivation();\n\
        var changedPrice = prices.firstEntity();\n\
        var initialPrice = prices.secondEntity();\n\
\n\
        // Validate cost transactions for item\n\
        costTransactions.query().forItem(item).assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(0).withVarianceQuantity(OnHandQuantity).withOnHandQuantity(OnHandQuantity)\n\
                                            .withFinancialReceipt().forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(DeltaPackingAndInvoice).withVarianceQuantity(OnHandQuantity-FirstInvoiceQuantity).withOnHandQuantity(OnHandQuantity-PackingSlipQuantity)\n\
                                            .withFinancialReceipt().withVoucher(changedPrice.parmStdCostVoucher()).forPrice(changedPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(-DeltaPackingAndInvoice).withVarianceQuantity(0).withOnHandQuantity(-(OnHandQuantity-PackingSlipQuantity))\n\
                                            .withFinancialIssue().withVoucher(changedPrice.parmStdCostVoucher()).forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(FirstInvoiceQuantity).withDeferredCogsQuantity(-FirstInvoiceQuantity).withVarianceQuantity(0).withOnHandQuantity(0)\n\
                                            .withFinancialIssue().withVoucher(firstInvoice.parmLedgerVoucherNumber()).forPrice(initialPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(SecondInvoiceQuantity).withDeferredCogsQuantity(-DeltaPackingAndInvoice).withVarianceQuantity(0).withOnHandQuantity(-(SalesQuantity-PackingSlipQuantity))\n\
                                            .withFinancialIssue().withVoucher(secondInvoice.parmLedgerVoucherNumber()).forPrice(changedPrice))\n\
            .addSpec(costTransactions.spec().withCogsQuantity(0).withDeferredCogsQuantity(PackingSlipQuantity).withVarianceQuantity(0).withOnHandQuantity(-PackingSlipQuantity)\n\
                                            .withPhysicalIssue().withVoucher(firstPackingSlip.parmLedgerVoucherNumber()).forPrice(initialPrice))\n\
            , 'Cost transactions for item');\n\
    }\n\
\n\
    private void setItemPrice(Price _price)\n\
    {\n\
        // Create and activate a standard cost price\n\
        invent.prices().initCostPrice()\n\
            .setVersion(costingVersion)     // Using the default costing version\n\
            .setItem(item)                  // For the default standard cost item\n\
            .setPrice(_price)               // With a given cost price\n\
            .save()                         // Save the item cost price\n\
            .activate();                    // Activate the item cost price\n\
\n\
        // Calculate standard cost price for the finished good based on the BOM\n\
        costingVersion.calculate().setItem(finishedGood).setQuantity(1).setProcurementMode(ItemProcurementMode::ProductionOrder).execute();\n\
    }\n\
\n\
}\n\
        </CostingSampleTest>\n\
                    /// <summary>\n\
/// The <c>InventCountingJournalSampleTest</c> class contains examples on creating counting journals.\n\
/// </summary>\n\
[SysTestCaseAutomaticNumberSequences]\n\
public final class InventCountingJournalSampleTest extends SysTestCase\n\
{\n\
    private const CostAmount                    CostPrice = 5.0;\n\
\n\
    private AtlDataRootNode                     data;\n\
    private AtlDataInvent                       invent;\n\
    private AtlDataInventTransactions           inventoryTransactions;\n\
    private AtlDataInventCountingJournals       countingJournals;\n\
    private AtlDataInventCountingJournalLines   countingJournalLines;\n\
    private AtlDataInventOnHand                 onHand;\n\
\n\
    private InventTable                         itemWithAllProductDimensions;\n\
    private InventSite                          site;\n\
    private InventLocation                      warehouse;\n\
    private EcoResColor                         colorRed, colorBlue;\n\
    private EcoResSize                          sizeMedium, sizeLarge;\n\
    private EcoResStyle                         styleA, styleB;\n\
\n\
    protected void initDataSetupReferences()\n\
    {\n\
        // Create data navigation variables\n\
        data = AtlDataRootNode::construct();\n\
\n\
        invent = data.invent();\n\
\n\
        inventoryTransactions = invent.trans();\n\
\n\
        countingJournals = invent.countingJournals();\n\
        countingJournalLines = invent.countingJournalLines();\n\
\n\
        onHand = data.invent().onHand();\n\
\n\
        // Create master data\n\
        site = invent.sites().default();                                            // Create default site\n\
        warehouse = invent.warehouses().default();                                  // Create default warehouse\n\
\n\
        var items = invent.items();\n\
\n\
        // Create standard cost item with color, size and style product dimensions enabled\n\
        itemWithAllProductDimensions = items.standardCostBuilder()\n\
                .setProductDimGroup(invent.productDimGroups().sizeColStl())\n\
                .create();\n\
\n\
        var products = data.products();\n\
\n\
        colorRed = products.colors().red();\n\
        colorBlue = products.colors().blue();\n\
\n\
        sizeMedium = products.sizes().medium();\n\
        sizeLarge = products.sizes().large();\n\
\n\
        styleA = products.styles().a();\n\
        styleB = products.styles().b();\n\
\n\
        items.createAndReleaseVariant(itemWithAllProductDimensions, [colorRed, sizeMedium, styleA]);    // Create product variant 1 - Red, Medium, Style A\n\
        items.createAndReleaseVariant(itemWithAllProductDimensions, [colorBlue, sizeLarge, styleB]);    // Create product variant 2 - Blue, Large, Style B\n\
\n\
        var costingVersion = data.cost().costingVersions().createDefaultStandard(); // Create default costing version of standard cost items\n\
\n\
        // Create and activate a standard cost price\n\
        invent.prices().initCostPrice()\n\
            .setVersion(costingVersion)             // Using the default costing version\n\
            .setItem(itemWithAllProductDimensions)  // For the default standard cost item\n\
            .setPrice(CostPrice)                    // With a given cost price\n\
            .save()                                 // Save the item cost price\n\
            .activate();                            // Activate the item cost price\n\
    }\n\
\n\
    public void setUp()\n\
    {\n\
        super();\n\
\n\
        this.initDataSetupReferences();\n\
    }\n\
\n\
    /// <summary>\n\
    /// Validates creation of counting journal and posting.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void createAndPostCountingJournal()\n\
    {\n\
        const InventQtyJournal  CountingJournalQuantityLine1 = 10;\n\
        const InventQtyJournal  CountingJournalQuantityLine2 = 15;\n\
        const CostAmount        CostAmountLine1 = CountingJournalQuantityLine1 * CostPrice;\n\
        const CostAmount        CostAmountLine2 = CountingJournalQuantityLine2 * CostPrice;\n\
\n\
        ttsbegin;\n\
\n\
        // Create counting journal\n\
        var journal = countingJournals.createDefault();\n\
\n\
        // Create first counting journal line\n\
        journal.addLine()                                                           // Add a new line on the counting journal\n\
            .setItem(itemWithAllProductDimensions)                                  // Using standard cost item\n\
            .setInventDims([colorRed, sizeMedium, styleA, warehouse])               // Using product dimensions Red, Medium and style A and default warehouse - site will be defaulted based on warehouse the same way as in the UI\n\
            .setQuantity(CountingJournalQuantityLine1)                              // Set the counting quantity\n\
            .save();                                                                // Save the counting journal line\n\
\n\
        // Create second counting journal line\n\
        journal.addLine()                                                           // Add a new line on the counting journal\n\
            .setItem(itemWithAllProductDimensions)                                  // Using standard cost item\n\
            .setInventDims([colorBlue, sizeLarge, styleB, warehouse])               // Using product dimensions Blue, Large and style B and default warehouse - site will be defaulted based on warehouse the same way as in the UI\n\
            .setQuantity(CountingJournalQuantityLine2)                              // Set the counting quantity\n\
            .save();                                                                // Save the counting journal line\n\
\n\
        // Validates inventory transactions for the counting journal\n\
        journal.inventoryTransactions().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(inventoryTransactions.spec()                                   // Add one specification to the expected results\n\
                .withQty(CountingJournalQuantityLine1)                              // The quantity should be the same as the counting line 1\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 1\n\
                .withInventDims([colorRed, sizeMedium, styleA, site, warehouse])    // The product dimensions should be Red, Medium and style A and default site and warehouse\n\
                .withCostAmountPhysical(0)                                          // Should not have a physical cost amount\n\
                .withStatusIssue(StatusIssue::None)                                 // Status issue should be none\n\
                .withStatusReceipt(StatusReceipt::Ordered)                          // Status receipt should be ordered\n\
                .withPhysicalDate(dateNull())                                       // Should not have a physical date\n\
                .withFinancialDate(dateNull())                                      // Should not have a financial date\n\
                .withValueOpen(InventTransOpen::Yes))                               // The open flag should be yes\n\
            .addSpec(inventoryTransactions.spec()                                   // Add one specification to the expected results\n\
                .withQty(CountingJournalQuantityLine2)                              // The quantity should be the same as the counting line 2\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 2\n\
                .withInventDims([colorBlue, sizeLarge, styleB, site, warehouse])    // The product dimensions should be Blue, Large and style B and default site and warehouse\n\
                .withCostAmountPhysical(0)                                          // Should not have a physical cost amount\n\
                .withStatusIssue(StatusIssue::None)                                 // Status issue should be none\n\
                .withStatusReceipt(StatusReceipt::Ordered)                          // Status receipt should be ordered\n\
                .withPhysicalDate(dateNull())                                       // Should not have a physical date\n\
                .withFinancialDate(dateNull())                                      // Should not have a financial date\n\
                .withValueOpen(InventTransOpen::Yes))                               // The open flag should be yes\n\
            , 'Inventory transactions after creating the counting journal.');\n\
\n\
        // Validate counting journal lines\n\
        journal.lines().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(countingJournalLines.spec()                                    // Add one specification to the expected results\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line\n\
                .withQuantity(CountingJournalQuantityLine1)                         // The quantity should be the same as the counting line 1\n\
                .withCostAmount(CostAmountLine1))                                   // Cost amount should be quantity * post price\n\
            .addSpec(countingJournalLines.spec()                                    // Add one specification to the expected results\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line\n\
                .withQuantity(CountingJournalQuantityLine2)                         // The quantity should be the same as the counting line 2\n\
                .withCostAmount(CostAmountLine2))                                   // Cost amount should be quantity * post price\n\
            , 'Journal lines after creating the counting journal.');\n\
\n\
        TransDate postingDate = DateTimeUtil::date(DateTimeUtil::applyTimeZoneOffset(DateTimeUtil::utcNow(), DateTimeUtil::getUserPreferredTimeZone()));\n\
\n\
        // Post the counting journal\n\
        journal.post();\n\
\n\
        // Validates inventory transactions for the counting journal after posting journal\n\
        journal.inventoryTransactions().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(inventoryTransactions.spec()                                   // Add one specification to the expected results\n\
                .withQty(CountingJournalQuantityLine1)                              // The quantity should be the same as the counting line 1\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 1\n\
                .withInventDims([colorRed, sizeMedium, styleA, site, warehouse])    // The product dimensions should be Red, Medium and style A and default site and warehouse\n\
                .withCostAmountPhysical(CostAmountLine1)                            // Cost amount should be quantity * post price\n\
                .withStatusIssue(StatusIssue::None)                                 // Status issue should be none\n\
                .withStatusReceipt(StatusReceipt::Purchased)                        // Status receipt should be purchased\n\
                .withPhysicalDate(postingDate)                                      // Should have a physical date\n\
                .withFinancialDate(postingDate)                                     // Should have a financial date\n\
                .withValueOpen(InventTransOpen::Yes))                               // The open flag should be yes\n\
            .addSpec(inventoryTransactions.spec()                                   // Add one specification to the expected results\n\
                .withQty(CountingJournalQuantityLine2)                              // The quantity should be the same as the counting line 2\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 2\n\
                .withInventDims([colorBlue, sizeLarge, styleB, site, warehouse])    // The product dimensions should be Blue, Large and style B and default site and warehouse\n\
                .withCostAmountPhysical(CostAmountLine2)                            // Cost amount should be quantity * post price\n\
                .withStatusIssue(StatusIssue::None)                                 // Status issue should be none\n\
                .withStatusReceipt(StatusReceipt::Purchased)                        // Status receipt should be purchased\n\
                .withPhysicalDate(postingDate)                                      // Should have a physical date\n\
                .withFinancialDate(postingDate)                                     // Should have a financial date\n\
                .withValueOpen(InventTransOpen::Yes))                               // The open flag should be yes\n\
            , 'Inventory transactions after posting the counting journal.');\n\
\n\
        // Validate counting journal lines after posting journal\n\
        journal.lines().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(countingJournalLines.spec()                                    // Add one specification to the expected results\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 1\n\
                .withQuantity(CountingJournalQuantityLine1)                         // The quantity should be the same as the counting line 1\n\
                .withCostAmount(CostAmountLine1))                                   // Cost amount should be quantity * post price\n\
            .addSpec(countingJournalLines.spec()                                    // Add one specification to the expected results\n\
                .withItem(itemWithAllProductDimensions)                             // Item should be the same as on the counting line 2\n\
                .withQuantity(CountingJournalQuantityLine2)                         // The quantity should be the same as the counting line 2\n\
                .withCostAmount(CostAmountLine2))                                   // Cost amount should be quantity * post price\n\
            , 'Journal lines after posting the counting journal.');\n\
\n\
        // Validate on-hand after posting journal\n\
        invent.onHand().assertExpectedOnHand(\n\
            onHand.spec().forItem(itemWithAllProductDimensions)                     // Add one specification to the expected results for item\n\
                .withInventDims([colorRed, sizeMedium, styleA, site, warehouse])    // The product dimensions should be Red, Medium and style A and default site and warehouse\n\
                .withAvailPhysical(CountingJournalQuantityLine1)                    // The available physical quantity should be the same as the counting line 1\n\
                .withAvailTotal(CountingJournalQuantityLine1),                      // The available total quantity should be the same as the counting line 1\n\
            onHand.spec().forItem(itemWithAllProductDimensions)                     // Add one specification to the expected results for item\n\
                .withInventDims([colorBlue, sizeLarge, styleB, site, warehouse])    // The product dimensions should be Blue, Large and style B and default site and warehouse\n\
                .withAvailPhysical(CountingJournalQuantityLine2)                    // The available physical quantity should be the same as the counting line 2\n\
                .withAvailTotal(CountingJournalQuantityLine2));                     // The available total quantity should be the same as the counting line 2\n\
\n\
        ttsabort;\n\
    }\n\
\n\
}\n\
// <summary>\n\
/// The <c>LedgerSampleTest</c> class contains examples on creating and validating ledger journals.\n\
/// </summary>\n\\n\
[SysTestCaseDataDependency('USMF')]\n\\n\
public final class LedgerSampleTest extends SysTestCase\n\\n\
{\n\
    private AtlDataRootNode                     data;\n\
    private AtlDataLedger                       ledger;\n\
    private AtlDataLedgerJournals               ledgerJournals;\n\
    private AtlDataGeneralJournals              ledgerGeneralJournals;\n\
    private AtlDataGeneralJournalAccountEntries accountEntries;\n\
\n\
    protected void initDataSetupReferences()\n\
    {\n\
        // Create data navigation variables\n\
        data = AtlDataRootNode::construct();\n\
\n\
        ledger = data.ledger();\n\
        ledgerJournals = ledger.ledgerJournals();\n\
        ledgerGeneralJournals = ledger.generalJournals();\n\
        accountEntries = ledger.generalJournalAccountEntries();\n\
    }\n\
\n\
    public void setUp()\n\
    {\n\
        super();\n\
\n\
        this.initDataSetupReferences();\n\
    }\n\
\n\
    /// <summary>\n\
    /// Validates creation of ledger journal and posting.\n\
    /// </summary>\n\
    [SysTestMethod]\n\
    public void createAndPostLedgerJournal()\n\
    {\n\
        const CurrencyCode TransactionCurrencyCode = 'EUR';\n\
        const ExchRate TransactionExchangeRate = 80;\n\
        const AmountCur TransactionAmount = 100;\n\
\n\
        // Create ledger journal\n\
        var postingDate1 = ledgerGeneralJournals.getFiscalYearStartDateWithNoActivity();\n\
        var postingDate2 = nextMth(postingDate1);\n\
\n\
        var journalHeader = AtlEntityJournalHeader::construct().setJournalName(ledgerJournals.dailyJournalName()).save();\n\
\n\
        LedgerDimensionAccount balanceSheet = new AtlLedgerDimensionAccountResolver()\n\
            .withDimension(DimensionAttribute::find(DimensionAttribute::getWellKnownDimensionAttribute(DimensionAttributeType::MainAccount)).Name, DemoDataValuesForUSMF::MainAccountBankAccountUSD)\n\
            .resolveReference();\n\
\n\
        LedgerDimensionAccount profitAndLoss = new AtlLedgerDimensionAccountResolver()\n\
            .withDimension(DimensionAttribute::find(DimensionAttribute::getWellKnownDimensionAttribute(DimensionAttributeType::MainAccount)).Name, DemoDataValuesForUSMF::MainAccountPostableExpense)\n\
            .resolveReference();\n\
\n\
        journalHeader.addLine().setDate(postingDate1)\n\
            .setCurrencyCode(TransactionCurrencyCode)\n\
            .setExchangeRate(TransactionExchangeRate)\n\
            .setLedgerPrimary(balanceSheet)\n\
            .setCreditAmount(TransactionAmount)\n\
            .setLedgerOffset(profitAndLoss);\n\
\n\
        journalHeader.save();\n\
\n\
        // Post the ledger journal\n\
        journalHeader.post();\n\
\n\
        // Validates transactions for the ledger journal after posting journal\n\
        journalHeader.lines().firstEntity().voucher().assertExpectedLinesSet(AtlSpecifications::construct()\n\
            .addSpec(accountEntries.spec().withAmount(TransactionExchangeRate))\n\
            .addSpec(accountEntries.spec().withAmount(-TransactionExchangeRate))\n\
            , 'Account entries after posting journal.');\n\
    }\n\
\n\
}",



    "system_small_prompt": "You are an expert in the programming language X++.",
    "system_medium_prompt": "You are an expert in creating Acceptance Tests for Dynamics 365 For Finance And Operations using the X++ Programming Language.\n\
Based on the ATLQuery, ATLSpecification and the ATLEntity you can always create tests using the Acceptance Test Library that cover import test cases and cover most situations.\n\
The code that is generated does compile and is based on examples that are given in the prompt.\n\
You think step by step.",
    "system_large_prompt": "You are an expert in creating Acceptance Tests for Dynamics 365 For Finance And Operations using the X++ Programming Language.\n\
Based on the ATLQuery, ATLSpecification and the ATLEntity you can always create tests using the Acceptance Test Library that cover import test cases and cover most situations.\n\
The code that is generated does compile and is based on examples that are given in the prompt.\n\
You think step by step.\n\
When creating Acceptance Tests using the X++ Acceptance Test Library (ATL), you follow these guidelines:\n\
\n\
Use the ATL framework classes such as ATLQuery, ATLSpecification, and ATLEntity to structure and organize your tests effectively.\n\
Leverage the power of ATLQuery to define test data and set up prerequisites for your tests. You can use ATLQuery to insert, update, or delete data in the database as needed.\n\
Utilize ATLSpecification to define the expected behavior and outcomes of your tests. You can use ATLSpecification to assert conditions, validate data, and check for specific results.\n\
Take advantage of ATLEntity to interact with the application's business logic and data model. You can use ATLEntity to create, read, update, and delete records in the system.\n\
Follow the Arrange-Act-Assert pattern when structuring your test methods. Use the Arrange section to set up the necessary test data and prerequisites, the Act section to perform the actions being tested, and the Assert section to verify the expected outcomes.\n\
Ensure that your tests are independent and self-contained. Each test should be able to run independently without relying on the state of other tests.\n\
Use meaningful and descriptive names for your test methods and variables to enhance readability and maintainability of your test code.\n\
Handle exceptions and error scenarios gracefully in your tests. Use try-catch blocks to catch and handle expected exceptions, and use assertions to validate error messages or specific exception types.\n\
Consider using data-driven testing techniques when applicable. You can use data providers or parameterized tests to run the same test logic with different sets of input data.\n\
Maintain good code organization and follow the coding conventions and best practices specific to X++ and the Dynamics 365 For Finance And Operations development guidelines.\n\
\n\
Remember, the goal is to create robust, reliable, and maintainable Acceptance Tests that cover various scenarios and ensure the quality and functionality of your Dynamics 365 For Finance And Operations implementation."}
