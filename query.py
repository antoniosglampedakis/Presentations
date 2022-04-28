Query = \
'''
select ed.FestivalCode, ed.FestivalYear, ed.Title, ed.Advertiser, ed.Product, 
ed.AwardCountCode as Winner, ed.Short as Shortlist, ed.EntryTypeName, ed.EntryId as "All Entries",
cd.companyName, cd.Country, cd.coTown, cd.NetworkName, cd.UltimateHoldingCompanyName, cd.RegionName,
ideacompany.companyName as "creativeAgency"

from PublishedArchiveEntryData ED

left Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId


left join  [ArchiveCompanyData] as ideacompany
	on ed.AgencyCompanyNoTwo = ideacompany.companyNo
	and ed.FestivalYear = ideacompany.ArchiveYear
left join

Where
ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
and ed.FestivalYear >= 2018
and ed.Cancelled !=1

'''



pgquery ='''
select distinct 
ed.FestivalCode, ed.FestivalYear, ed.Title, ed.Advertiser, ed.Product, 
ed.AwardCountCode as Winner, ed.Short as Shortlist, ed.EntryTypeName, ed.EntryId as "All Entries",
cd.companyName, cd.Country, cd.coTown, cd.NetworkName, cd.UltimateHoldingCompanyName, cd.RegionName

from ArchiveEntryData ED

left Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

where (Advertiser  like '%p&g%'
or Advertiser  like '%PROCTER & GAMBLE%' 
or Advertiser   like '%PROCTER&GAMBLE%' )
and ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')

and ed.FestivalYear >= 2020
--and short = 1
order by ed.festivalYear, title
'''

OrlaAsiaQuery ='''
select cd.Country,  ed.FestivalYear, cd.RegionName, ed.short, ed.AwardCountCode as Winners, ed.entryId as count
from ArchiveEntryData ED

inner Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

where ed.FestivalYear >= 2017
'''


QueryIndAgency ='''
select cd.companyName, cd.CompanyType, cd.coTown, cd.RegionName, cd.Country, cd.NetworkName,
ed.FestivalYear, ed.FestivalCode, ed.Short, ed.AwardCountCode, ed.Title, ed.Advertiser, ed.Product, ed.EntryId, ed.EntryTypeName

from ArchiveCompanyData cd

left Join ArchiveEntryData as ed
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

where ArchiveYear >= 2011

--and ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
and (cd.NetworkName is null
or cd.networkname = 'ALL OTHER COMPANIES'
or cd.networkname = '- no network -'
or cd.networkname = '- no network (legacy DO NOT PICK) -'
)
and(
cd.companytype != 'other'
and cd.companytype != 'Technology'
and cd.companytype != 'ADVERTISER/CLIENT'
and cd.companytype != 'INTERNET')

'''

QuerySaLatest = '''
select 

ed.FestivalCode, ed.FestivalYear, ed.Title, ed.Advertiser, ed.Product, 
ed.AwardCountCode as Winner, ed.Short as Shortlist, ed.EntryTypeName, ed.EntryId as "All Entries",
cd.companyName, cd.Country, cd.coTown, cd.NetworkName, cd.UltimateHoldingCompanyName, cd.RegionName

from ArchiveEntryData ED

left Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear


where ed.festivalcode like '%sa%'
order by ed.FestivalYear
'''

QueryForEdelmanOtherFields = '''
select ed.FestivalCode, ed.FestivalYear, ed.Title, ed.Advertiser, ed.Product, 
ed.AwardCountCode as Winner, ed.Short as Shortlist, ed.EntryTypeName, ed.EntryId as "All Entries",
cd.companyName, cd.Country, cd.coTown, cd.NetworkName, cd.UltimateHoldingCompanyName, cd.RegionName,
AgencyCompanyNo.companyName as "creativeAgency",
AgencyCompanyNoTwo.companyName as "creativeAgency2"


from PublishedArchiveEntryData ED

left Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId


left join  [ArchiveCompanyData] as AgencyCompanyNo
	on ed.AgencyCompanyNo = AgencyCompanyNo.companyNo
	and ed.FestivalYear = AgencyCompanyNo.ArchiveYear

left join  [ArchiveCompanyData] as AgencyCompanyNoTwo
	on ed.AgencyCompanyNoTwo = AgencyCompanyNoTwo.companyNo
	and ed.FestivalYear = AgencyCompanyNoTwo.ArchiveYear



Where
ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
and ed.FestivalYear >= 2018
and ed.Cancelled !=1

'''