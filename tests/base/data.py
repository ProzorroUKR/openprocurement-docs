# -*- coding: utf-8 -*-
from copy import deepcopy

from datetime import timedelta
from openprocurement.api.utils import get_now
from hashlib import sha512
from uuid import uuid4

parameters = [
    {'code': 'OCDS-123454-AIR-INTAKE', 'value': 0.1},
    {'code': 'OCDS-123454-YEARS', 'value': 0.1}
]

tenderer = {
    "address": {
        "countryName": "Україна",
        "locality": "м. Вінниця",
        "postalCode": "21100",
        "region": "м. Вінниця",
        "streetAddress": "вул. Островського, 33"
    },
    "contactPoint": {
        "email": "soleksuk@gmail.com",
        "name": "Сергій Олексюк",
        "telephone": "+380 (432) 21-69-30"
    },
    "identifier": {
        "scheme": u"UA-EDR",
        "id": u"00137256",
        "uri": u"http://www.sc.gov.ua/"
    },
    "name": "ДКП «Школяр»"
}

tenderer2 = {
    "address": {
        "countryName": "Україна",
        "locality": "м. Львів",
        "postalCode": "79013",
        "region": "м. Львів",
        "streetAddress": "вул. Островського, 34"
    },
    "contactPoint": {
        "email": "aagt@gmail.com",
        "name": "Андрій Олексюк",
        "telephone": "+380 (322) 91-69-30"
    },
    "identifier": {
        "scheme": u"UA-EDR",
        "id": u"00137226",
        "uri": u"http://www.sc.gov.ua/"
    },
    "name": "ДКП «Книга»"
}

tenderer3 = {
    "address": {
        "countryName": "Україна",
        "locality": "м. Львів",
        "postalCode": "79013",
        "region": "м. Львів",
        "streetAddress": "вул. Островського, 35"
    },
    "contactPoint": {
        "email": "fake@mail.com",
        "name": "Іван Іваненко",
        "telephone": "+380 (322) 12-34-56"
    },
    "identifier": {
        "scheme": u"UA-EDR",
        "id": u"00137227",
        "uri": u"http://www.sc.gov.ua/"
    },
    "name": "«Снігур»"
}

tenderer4 = {
    "address": {
        "countryName": "Україна",
        "locality": "м. Запоріжя",
        "postalCode": "79013",
        "region": "м. Запоріжжя",
        "streetAddress": "вул. Коцюбинського, 15"
    },
    "contactPoint": {
        "email": "fake@mail.com",
        "name": "Іван Карпенко",
        "telephone": "+380 (322) 12-34-56"
    },
    "identifier": {
        "scheme": u"UA-EDR",
        "id": u"00137228",
        "uri": u"http://www.sc.gov.ua/"
    },
    "name": "«Кенгуру»"
}

bad_participant = {
    "address": {
        "countryName": "Україна",
        "locality": "м. Львів",
        "postalCode": "21100",
        "region": "м. Львів",
        "streetAddress": "вул. Поле, 33"
    },
    "contactPoint": {
        "email": "pole@gmail.com",
        "name": "Вільям Поле",
        "telephone": "+380 (452) 21-69-31"
    },
    "identifier": {
        "id": "00137230",
        "legalName": "ТОВ Бур",
        "scheme": "UA-EDR",
        "uri": "http://pole.edu.vn.ua/"
    },
    "name": "ТОВ \"Бур\""
}

bid_document = {
    'title': u'Proposal_part1.pdf',
    'url': u"http://broken1.ds",
    'hash': 'md5:' + '0' * 32,
    'format': 'application/pdf',
}

bid_document2 = {
    'title': u'Proposal_part2.pdf',
    'url': u"http://broken2.ds",
    'hash': 'md5:' + '0' * 32,
    'format': 'application/pdf',
}

bid_document3_eligibility = {
    'title': u'eligibility_doc.pdf',
    'url': u"http://broken3.ds",
    'hash': 'md5:' + '0' * 32,
    'format': 'application/pdf',
}

bid_document4_financialy = {
    'title': u'financial_doc.pdf',
    'url': u"http://broken4.ds",
    'hash': 'md5:' + '0' * 32,
    'format': 'application/pdf',
}

bid_document5_qualification = {
    'title': u'qualification_document.pdf',
    'url': u"http://broken5.ds",
    'hash': 'md5:' + '0' * 32,
    'format': 'application/pdf',
}

bid = {
    "tenderers": [tenderer],
    "value": {
        "amount": 500
    }
}

bid_draft = deepcopy(bid)
bid_draft["status"] = "draft"

bid2 = {
    "tenderers": [tenderer2],
    "value": {
        "amount": 499
    }
}

bid2_with_docs = deepcopy(bid2)
bid2_with_docs["documents"] = [bid_document, bid_document2]

bid3 = {
    "tenderers": [tenderer3],
    "value": {
        "amount": 5
    }
}

bid3_with_docs = deepcopy(bid2)
bid3_with_docs["documents"] = [bid_document, bid_document2]
bid3_with_docs["eligibilityDocuments"] = [bid_document3_eligibility]
bid3_with_docs["financialDocuments"] = [bid_document4_financialy]
bid3_with_docs["qualificationDocuments"] = [bid_document5_qualification]

bid4 = {
    "tenderers": [tenderer4],
    "value": {
        "amount": 5
    }
}

lot_uid = uuid4().hex

lot_bid = {
    "tenderers": [tenderer],
    "status": "draft",
    "lotValues": [{
        "value": {
            "amount": 500
        },
        "relatedLot": lot_uid
    }]

}

lot_bid2 = {
    "tenderers": [tenderer2],
    "lotValues": [{
        "value": {
            "amount": 499
        },
        "relatedLot": lot_uid
    }]
}

lot_bid2_with_docs = deepcopy(lot_bid2)
lot_bid2_with_docs["documents"] = [bid_document, bid_document2]

lot_bid3 = {
    "tenderers": [tenderer3],
    "lotValues": [{
        "value": {
            "amount": 5
        },
        "relatedLot": lot_uid
    }]
}

lot_bid3_with_docs = deepcopy(lot_bid3)
lot_bid3_with_docs["documents"] = [bid_document, bid_document2]
lot_bid3_with_docs["eligibilityDocuments"] = [bid_document3_eligibility]
lot_bid3_with_docs["financialDocuments"] = [bid_document4_financialy]
lot_bid3_with_docs["qualificationDocuments"] = [bid_document5_qualification]

question = {
    "author": tenderer2,
    "description": "Просимо додати таблицю потрібної калорійності харчування",
    "title": "Калорійність"
}

test_max_uid = uuid4().hex

features = [
    {
        "code": "OCDS-123454-AIR-INTAKE",
        "featureOf": "item",
        "relatedItem": test_max_uid,
        "title": u"Потужність всмоктування",
        "title_en": "Air Intake",
        "description": u"Ефективна потужність всмоктування пилососа, в ватах (аероватах)",
        "enum": [
            {
                "value": 0.1,
                "title": u"До 1000 Вт"
            },
            {
                "value": 0.15,
                "title": u"Більше 1000 Вт"
            }
        ]
    },
    {
        "code": "OCDS-123454-YEARS",
        "featureOf": "tenderer",
        "title": u"Років на ринку",
        "title_en": "Years trading",
        "description": u"Кількість років, які організація учасник працює на ринку",
        "enum": [
            {
                "value": 0.05,
                "title": u"До 3 років"
            },
            {
                "value": 0.1,
                "title": u"Більше 3 років, менше 5 років"
            },
            {
                "value": 0.15,
                "title": u"Більше 5 років"
            }
        ]
    }
]

funder = {
    "additionalIdentifiers": [],
    "address": {
        "countryName": "Switzerland",
        "locality": "Geneva",
        "postalCode": "1218",
        "region": "Grand-Saconnex",
        "streetAddress": "Global Health Campus, Chemin du Pommier 40"
    },
    "contactPoint": {
        "email": "ccm@theglobalfund.org",
        "faxNumber": "+41 44 580 6820",
        "name": "",
        "telephone": "+41 58 791 1700",
        "url": "https://www.theglobalfund.org/en/"
    },
    "identifier": {
        "id": "47045",
        "legalName": "Глобальний Фонд для боротьби зі СНІДом, туберкульозом і малярією",
        "scheme": "XM-DAC"
    },
    "name": "Глобальний фонд"
}

complaint = {
    "description": "Умови виставлені замовником не містять достатньо інформації, щоб заявка мала сенс.",
    "title": "Недостатньо інформації",
    'author': tenderer
}

qualified = {
    'selfEligible': True,
    'selfQualified': True
}

subcontracting = {
    'subcontractingDetails': "ДКП «Орфей», Україна"
}

lots = [
    {
        'title': 'Лот №1',
        'description': 'Опис Лот №1',
    },
    {
        'title': 'Лот №2',
        'description': 'Опис Лот №2',
    }
]

items = [
    {
        "id": test_max_uid,
        "description": u"футляри до державних нагород",
        "description_en": u"Cases with state awards",
        "description_ru": u"футляры к государственным наградам",
        "classification": {
            "scheme": u"ДК021",
            "id": u"44617100-9",
            "description": u"Cartons"
        },
        "additionalClassifications": [
            {
                "scheme": u"ДКПП",
                "id": u"17.21.1",
                "description": u"папір і картон гофровані, паперова й картонна тара"
            }
        ],
        "unit": {
            "name": u"item",
            "code": u"44617100-9"
        },
        "quantity": 5
    }
]

items_en = [
    {
        "additionalClassifications": [
            {
                "scheme": "ДКПП",
                "id": "17.21.1",
                "description": "Послуги шкільних їдалень"
            }
        ],
        "description": "Послуги шкільних їдалень",
        "description_en": "Services in school canteens",
        "classification": {
            "scheme": "ДК021",
            "id": "37810000-9",
            "description": "Test"
        },
        "deliveryDate": {
            "startDate": (get_now() + timedelta(days=20)).isoformat(),
            "endDate": (get_now() + timedelta(days=50)).isoformat()
        },
        "deliveryAddress": {
            "countryName": u"Україна",
            "postalCode": "79000",
            "region": u"м. Київ",
            "locality": u"м. Київ",
            "streetAddress": u"вул. Банкова 1"
        },
        "quantity": 1
    }, {
        "additionalClassifications": [
            {
                "scheme": "ДКПП",
                "id": "17.21.1",
                "description": "Послуги шкільних їдалень"
            }
        ],
        "description": "Послуги шкільних їдалень",
        "description_en": "Services in school canteens",
        "classification": {
            "scheme": "ДК021",
            "id": "37810000-9",
            "description": "Test"
        },
        "quantity": 1,
        "deliveryDate": {
            "startDate": (get_now() + timedelta(days=20)).isoformat(),
            "endDate": (get_now() + timedelta(days=50)).isoformat()
        },
        "deliveryAddress": {
            "countryName": u"Україна",
            "postalCode": "79000",
            "region": u"м. Київ",
            "locality": u"м. Київ",
            "streetAddress": u"вул. Банкова 1"
        }
    }
]

items_en_unit = deepcopy(items_en)
items_en_unit[0].update({
    "unit": {
        "code": "44617100-9",
        "name": "item"
    }
})
items_en_unit[1].update({
    "unit": {
        "code": "44617100-9",
        "name": "item"
    }
})

items_ua = [
    {
        "additionalClassifications": [
            {
                "scheme": "ДКПП",
                "id": "17.21.1",
                "description": "Послуги шкільних їдалень"
            }
        ],
        "description": "Послуги шкільних їдалень",
        "deliveryDate": {
            "startDate": (get_now() + timedelta(days=20)).isoformat(),
            "endDate": (get_now() + timedelta(days=50)).isoformat()
        },
        "deliveryAddress": {
            "countryName": u"Україна",
            "postalCode": "79000",
            "region": u"м. Київ",
            "locality": u"м. Київ",
            "streetAddress": u"вул. Банкова 1"
        },
        "classification": {
            "description": "Послуги з харчування у школах",
            "id": "55523100-3",
            "scheme": "ДК021"
        },
        "quantity": 1
    }
]

items_ua_unit = deepcopy(items_ua)
items_ua_unit[0].update({
    "unit": {
        "code": "44617100-9",
        "name": "item"
    }
})

procuring_entity = {
    "name": u"Державне управління справами",
    "identifier": {
        "scheme": u"UA-EDR",
        "id": u"00037256",
        "uri": u"http://www.dus.gov.ua/"
    },
    "address": {
        "countryName": u"Україна",
        "postalCode": u"01220",
        "region": u"м. Київ",
        "locality": u"м. Київ",
        "streetAddress": u"вул. Банкова, 11, корпус 1"
    },
    "contactPoint": {
        "name": u"Державне управління справами",
        "telephone": u"0440000000"
    },
    'kind': 'general'
}

procuring_entity_en = {
    "kind": "general",
    "address": {
        "countryName": "Україна",
        "locality": "м. Вінниця",
        "postalCode": "21027",
        "region": "м. Вінниця",
        "streetAddress": "вул. Стахурського. 22"
    },
    "contactPoint": {
        "name": "Куца Світлана Валентинівна",
        "name_en": "Kutsa Svitlana V.",
        "telephone": "+380 (432) 46-53-02",
        "availableLanguage": u"uk",
        "url": "http://sch10.edu.vn.ua/"
    },
    "identifier": {
        "id": "21725150",
        "legalName": "Заклад \"Загальноосвітня школа І-ІІІ ступенів № 10 Вінницької міської ради\"",
        "legalName_en": "The institution \"Secondary school I-III levels № 10 Vinnitsa City Council\"",
        "scheme": "UA-EDR"
    },
    "name": "ЗОСШ #10 м.Вінниці",
    "name_en": "School #10 of Vinnytsia"
}

procuring_entity_ua = {
    "kind": "special",
    "address": {
        "countryName": "Україна",
        "locality": "м. Вінниця",
        "postalCode": "21027",
        "region": "м. Вінниця",
        "streetAddress": "вул. Стахурського. 22"
    },
    "contactPoint": {
        "name": "Куца Світлана Валентинівна",
        "telephone": "+380 (432) 46-53-02",
        "url": "http://sch10.edu.vn.ua/"
    },
    "identifier": {
        "id": "21725150",
        "legalName": "Заклад \"Загальноосвітня школа І-ІІІ ступенів № 10 Вінницької міської ради\"",
        "scheme": "UA-EDR"
    },
    "name": "ЗОСШ #10 м.Вінниці"
}

shortlisted_firms = [
    {
        "identifier": {
            "scheme": u"UA-EDR",
            "id": u'00137256',
            "uri": u'http://www.sc.gov.ua/'
        },
        "name": "ДКП «Школяр»"
    },
    {
        "identifier": {
            "scheme": u"UA-EDR",
            "id": u'00137226',
            "uri": u'http://www.sc.gov.ua/'
        },
        "name": "ДКП «Книга»"
    },
    {
        "identifier": {
            "scheme": u"UA-EDR",
            "id": u'00137228',
            "uri": u'http://www.sc.gov.ua/'
        },
        "name": "«Кенгуру»",
    },
]

award = {
    "status": "pending",
    "suppliers": [tenderer],
    "value": {
        "amount": 475000,
        "currency": "UAH",
        "valueAddedTaxIncluded": True
    }
}

tender_below_maximum = {
    "title": u"футляри до державних нагород",
    "title_en": u"Cases with state awards",
    "title_ru": u"футляры к государственным наградам",
    "procuringEntity": procuring_entity,
    "value": {
        "amount": 500,
        "currency": u"UAH"
    },
    "minimalStep": {
        "amount": 35,
        "currency": u"UAH"
    },
    "items": items,
    "enquiryPeriod": {
        "endDate": (get_now() + timedelta(days=7)).isoformat()
    },
    "tenderPeriod": {
        "endDate": (get_now() + timedelta(days=14)).isoformat()
    },
    "procurementMethodType": "belowThreshold",
    "mode": u"test",
    "features": features
}

tender_cfaselectionua_maximum = {
    "title": u"футляри до державних нагород",
    "title_en": u"Cases with state awards",
    "title_ru": u"футляры к государственным наградам",
    "procuringEntity": {
        "name": u"Державне управління справами",
        "identifier": {
            "scheme": u"UA-EDR",
            "id": u"00037256",
            "uri": u"http://www.dus.gov.ua/"
        },
        "address": {
            "countryName": u"Україна",
            "postalCode": u"01220",
            "region": u"м. Київ",
            "locality": u"м. Київ",
            "streetAddress": u"вул. Банкова, 11, корпус 1"
        },
        "contactPoint": {
            "name": u"Державне управління справами",
            "telephone": u"0440000000"
        },
        'kind': 'general'
    },
    "items": items,
    "procurementMethodType": "closeFrameworkAgreementSelectionUA",
    "mode": u"test",
}

tender_stage1 = {
    "tenderPeriod": {
        "endDate": "2016-02-11T14:04:18.962451"
    },
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethodType": "competitiveDialogueEU",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "procuringEntity": procuring_entity_en,
    "items": items_en_unit
}

tender_stage2_multiple_lots = {
    "procurementMethod": "selective",
    "dialogue_token": sha512('secret').hexdigest(),
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethodType": "competitiveDialogueEU.stage2",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "shortlistedFirms": shortlisted_firms,
    "owner": "broker",
    "procuringEntity": procuring_entity_en,
    "items": items_en_unit
}

tender_stage2EU = {
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "procurementMethod": "selective",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "status": "draft",
    "procurementMethodType": "competitiveDialogueEU.stage2",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "dialogue_token": "",
    "shortlistedFirms": shortlisted_firms,
    "owner": "broker",
    "procuringEntity": procuring_entity_en,
    "items": items_en_unit
}

tender_stage2UA = {
    "title": "футляри до державних нагород",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethod": "selective",
    "procurementMethodType": "competitiveDialogueUA.stage2",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "status": "draft",
    "shortlistedFirms": shortlisted_firms,
    "owner": "broker",
    "procuringEntity": procuring_entity_ua,
    "items": items_ua_unit
}

tender_limited = {
    "items": items_ua,
    "owner": "broker",
    "procurementMethod": "limited",
    "procurementMethodType": "reporting",
    "status": "active",
    "procuringEntity": procuring_entity_ua,
    "value": {
        "amount": 500000,
        "currency": "UAH",
        "valueAddedTaxIncluded": True
    },
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "title_ru": "Услуги школьных столовых",
    "description_en": "Services in school canteens",
    "description_ru": "Услуги школьных столовых",
}

tender_openeu = {
    "tenderPeriod": {
        "endDate": (get_now() + timedelta(days=31)).isoformat()
    },
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethodType": "aboveThresholdEU",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "procuringEntity": procuring_entity_en,
    "items": items_en
}

tender_openua = {
    "tenderPeriod": {
        "endDate": (get_now() + timedelta(days=16)).isoformat()
    },
    "title": "футляри до державних нагород",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethodType": "aboveThresholdUA",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "procuringEntity": procuring_entity_ua,
    "items": items_ua
}

tender_esco = {
    "tenderPeriod": {
        "endDate": (get_now() + timedelta(days=31)).isoformat()
    },
    "title": "Послуги шкільних їдалень",
    "title_en": "Services in school canteens",
    "procurementMethodType": "esco",
    "minimalStepPercentage": 0.006,
    "procuringEntity": procuring_entity_en,
    "items": items_en_unit,
    "NBUdiscountRate": 0.22986,
    "fundingKind": "other",
    "yearlyPaymentsPercentageRange": 0.8
}

tender_defense = {
    "tenderPeriod": {
        "endDate": (get_now() + timedelta(days=16)).isoformat()
    },
    "title": "футляри до державних нагород",
    "minimalStep": {
        "currency": "UAH",
        "amount": 35
    },
    "procurementMethodType": "aboveThresholdUA.defense",
    "value": {
        "currency": "UAH",
        "amount": 500
    },
    "procuringEntity": procuring_entity_ua,
    "items": items_ua
}