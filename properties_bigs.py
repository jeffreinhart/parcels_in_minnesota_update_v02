from parcels_base_classes import countyEtlParams

def createCountyObj():

    countyObj = countyEtlParams()

    countyObj.county_name = 'Big Stone'
    countyObj.cty_fips = r'11'
    countyObj.county_id = r'011'
    countyObj.cty_abbr = r'BIGS'
    countyObj.mngeo_web_id = r'Big Stone 011'
    countyObj.sourceZipFile = r'BIGS_parcels.zip'
    countyObj.sourcePolygons = r'Parcel_TaxInfo.shp'
    countyObj.sourceOwnershipZipFile = r''
    countyObj.sourceOwnershipTable = r''
    countyObj.joinInField = r''
    countyObj.joinJoinField = r''
    countyObj.PIN_fieldList = ['PARCEL']
    countyObj.BLDG_NUM_fieldList = []
    countyObj.BLDG_NUM_transferType = 'defaultTransfer'
    countyObj.PREFIX_DIR_fieldList = []
    countyObj.PREFIX_DIR_transferType = 'defaultTransfer'
    countyObj.PREFIXTYPE_fieldList = []
    countyObj.PREFIXTYPE_transferType = 'defaultTransfer'
    countyObj.STREETNAME_fieldList = []
    countyObj.STREETNAME_transferType = 'defaultTransfer'
    countyObj.STREETTYPE_fieldList = []
    countyObj.STREETTYPE_transferType = 'defaultTransfer'
    countyObj.SUFFIX_DIR_fieldList = []
    countyObj.SUFFIX_DIR_transferType = 'defaultTransfer'
    countyObj.UNIT_INFO_fieldList = []
    countyObj.UNIT_INFO_transferType = 'defaultTransfer'
    countyObj.CITY_fieldList = []
    countyObj.CITY_transferType = 'defaultTransfer'
    countyObj.CITY_USPS_fieldList = []
    countyObj.CITY_USPS_transferType = 'defaultTransfer'
    countyObj.ZIP_fieldList = []
    countyObj.ZIP_transferType = 'defaultTransfer'
    countyObj.ZIP4_fieldList = []
    countyObj.ZIP4_transferType = 'defaultTransfer'
    countyObj.PLAT_NAME_fieldList = ['PlatName']
    countyObj.PLAT_NAME_transferType = 'defaultTransfer'
    countyObj.BLOCK_fieldList = ['APBLOK']
    countyObj.BLOCK_transferType = 'defaultTransfer'
    countyObj.LOT_fieldList = ['APLOT']
    countyObj.LOT_transferType = 'defaultTransfer'
    countyObj.ACRES_POLY_fieldList = []
    countyObj.ACRES_DEED_fieldList = []
    countyObj.USE1_DESC_fieldList = []
    countyObj.USE1_DESC_transferType = 'defaultTransfer'
    countyObj.USE2_DESC_fieldList = []
    countyObj.USE2_DESC_transferType = 'defaultTransfer'
    countyObj.USE3_DESC_fieldList = []
    countyObj.USE3_DESC_transferType = 'defaultTransfer'
    countyObj.USE4_DESC_fieldList = []
    countyObj.USE4_DESC_transferType = 'defaultTransfer'
    countyObj.MULTI_USES_fieldList = []
    countyObj.MULTI_USES_transferType = 'defaultTransfer'
    countyObj.LANDMARK_fieldList = []
    countyObj.LANDMARK_transferType = 'defaultTransfer'
    countyObj.OWNER_NAME_fieldList = ['TXPRNAME']
    countyObj.OWNER_NAME_transferType = 'defaultTransfer'
    countyObj.OWNER_MORE_fieldList = []
    countyObj.OWNER_MORE_transferType = 'defaultTransfer'
    countyObj.OWN_ADD_L1_fieldList = ['TXPRADR1']
    countyObj.OWN_ADD_L1_transferType = 'defaultTransfer'
    countyObj.OWN_ADD_L2_fieldList = ['TXPRADR2']
    countyObj.OWN_ADD_L2_transferType = 'defaultTransfer'
    countyObj.OWN_ADD_L3_fieldList = ['TXPRADR3']
    countyObj.OWN_ADD_L3_transferType = 'defaultTransfer'
    countyObj.OWN_ADD_L4_fieldList = ['TXPRCITY', 'TXPRSTATE', 'TAXZIP5']
    countyObj.OWN_ADD_L4_transferType = 'concatTruncateLastAddrLine'
    countyObj.TAX_NAME_fieldList = []
    countyObj.TAX_NAME_transferType = 'defaultTransfer'
    countyObj.TAX_ADD_L1_fieldList = []
    countyObj.TAX_ADD_L1_transferType = 'defaultTransfer'
    countyObj.TAX_ADD_L2_fieldList = []
    countyObj.TAX_ADD_L2_transferType = 'defaultTransfer'
    countyObj.TAX_ADD_L3_fieldList = []
    countyObj.TAX_ADD_L3_transferType = 'defaultTransfer'
    countyObj.TAX_ADD_L4_fieldList = []
    countyObj.TAX_ADD_L4_transferType = 'defaultTransfer'
    countyObj.OWNERSHIP_fieldList = []
    countyObj.OWNERSHIP_transferType = 'defaultTransfer'
    countyObj.HOMESTEAD_fieldList = []
    countyObj.HOMESTEAD_transferType = 'defaultTransfer'
    countyObj.TAX_YEAR_fieldList = []
    countyObj.MARKET_YEAR_fieldList = []
    countyObj.EMV_LAND_fieldList = []
    countyObj.EMV_BLDG_fieldList = []
    countyObj.EMV_TOTAL_fieldList = []
    countyObj.TAX_CAPAC_fieldList = []
    countyObj.TOTAL_TAX_fieldList = []
    countyObj.SPEC_ASSES_fieldList = []
    countyObj.TAX_EXEMPT_fieldList = []
    countyObj.TAX_EXEMPT_transferType = 'defaultTransfer'
    countyObj.XUSE1_DESC_fieldList = []
    countyObj.XUSE1_DESC_transferType = 'defaultTransfer'
    countyObj.XUSE2_DESC_fieldList = []
    countyObj.XUSE2_DESC_transferType = 'defaultTransfer'
    countyObj.XUSE3_DESC_fieldList = []
    countyObj.XUSE3_DESC_transferType = 'defaultTransfer'
    countyObj.XUSE4_DESC_fieldList = []
    countyObj.XUSE4_DESC_transferType = 'defaultTransfer'
    countyObj.DWELL_TYPE_fieldList = []
    countyObj.DWELL_TYPE_transferType = 'defaultTransfer'
    countyObj.HOME_STYLE_fieldList = []
    countyObj.HOME_STYLE_transferType = 'defaultTransfer'
    countyObj.FIN_SQ_FT_fieldList = []
    countyObj.GARAGE_fieldList = []
    countyObj.GARAGE_transferType = 'defaultTransfer'
    countyObj.GARAGESQFT_fieldList = []
    countyObj.BASEMENT_fieldList = []
    countyObj.BASEMENT_transferType = 'defaultTransfer'
    countyObj.HEATING_fieldList = []
    countyObj.HEATING_transferType = 'defaultTransfer'
    countyObj.COOLING_fieldList = []
    countyObj.COOLING_transferType = 'defaultTransfer'
    countyObj.YEAR_BUILT_fieldList = []
    countyObj.NUM_UNITS_fieldList = []
    countyObj.SALE_DATE_fieldList = []
    countyObj.SALE_DATE_transferType = 'ToDate'
    countyObj.SALE_VALUE_fieldList = []
    countyObj.SCHOOL_DST_fieldList = ['SchoolName']
    countyObj.SCHOOL_DST_transferType = 'defaultTransfer'
    countyObj.WSHD_DIST_fieldList = []
    countyObj.WSHD_DIST_transferType = 'defaultTransfer'
    countyObj.GREEN_ACRE_fieldList = []
    countyObj.GREEN_ACRE_transferType = 'defaultTransfer'
    countyObj.OPEN_SPACE_fieldList = []
    countyObj.OPEN_SPACE_transferType = 'defaultTransfer'
    countyObj.AG_PRESERV_fieldList = []
    countyObj.AG_PRESERV_transferType = 'defaultTransfer'
    countyObj.AGPRE_ENRD_fieldList = []
    countyObj.AGPRE_ENRD_transferType = 'ToDate'
    countyObj.AGPRE_EXPD_fieldList = []
    countyObj.AGPRE_EXPD_transferType = 'ToDate'
    countyObj.PARC_CODE_fieldList = []
    countyObj.SECTION_fieldList = ['APSECT']
    countyObj.TOWNSHIP_fieldList = ['APTOWN']
    countyObj.RANGE_fieldList = ['APRANG']
    countyObj.RANGE_DIR_fieldList = []
    countyObj.LEGAL_DESC_fieldList = ['LEGAL']
    countyObj.LEGAL_DESC_transferType = 'defaultTransfer'
    countyObj.EDIT_DATE_fieldList = []
    countyObj.EDIT_DATE_transferType = 'ToDate'
    countyObj.EXPORT_DATE_fieldList = []
    countyObj.EXPORT_DATE_transferType = 'ToDate'
    countyObj.ORIG_PIN_fieldList = ['PARCEL']
    countyObj.ORIG_PIN_transferType = 'defaultTransfer'

    return countyObj
