# -*- coding: utf-8 -*-
import os
from copy import deepcopy
from datetime import timedelta

from openprocurement.api.utils import get_now
from openprocurement.planning.api.tests.base import BasePlanWebTest
from openprocurement.planning.api.tests.base import test_plan_data

from tests.base.constants import DOCS_URL
from tests.base.test import DumpsWebTestApp, MockWebTestMixin

TARGET_DIR = 'docs/source/planning/tutorial/'

test_plan_data = deepcopy(test_plan_data)


class PlanResourceTest(BasePlanWebTest, MockWebTestMixin):
    AppClass = DumpsWebTestApp

    relative_to = os.path.dirname(__file__)
    initial_data = test_plan_data
    docservice = True
    docservice_url = DOCS_URL

    def setUp(self):
        super(PlanResourceTest, self).setUp()
        self.setUpMock()

    def tearDown(self):
        self.tearDownMock()
        super(PlanResourceTest, self).tearDown()

    def create_plan(self):
        pass

    def test_docs(self):
        self.app.authorization = ('Basic', ('broker', ''))
        # empty plans listing
        response = self.app.get('/plans')
        self.assertEqual(response.json['data'], [])

        # create plan
        test_plan_data['tender'].update({"tenderPeriod": {"startDate": (get_now() + timedelta(days=7)).isoformat()}})
        test_plan_data['items'][0].update({"deliveryDate": {"endDate": (get_now() + timedelta(days=15)).isoformat()}})
        test_plan_data['items'][1].update({"deliveryDate": {"endDate": (get_now() + timedelta(days=16)).isoformat()}})
        test_plan_data['items'][2].update({"deliveryDate": {"endDate": (get_now() + timedelta(days=17)).isoformat()}})

        with open(TARGET_DIR + 'create-plan.http', 'w') as self.app.file_obj:
            response = self.app.post_json(
                '/plans?opt_pretty=1',
                {'data': test_plan_data})
            self.assertEqual(response.status, '201 Created')

        plan = response.json['data']
        plan_id = self.plan_id = response.json['data']['id']
        owner_token = response.json['access']['token']

        with open(TARGET_DIR + 'example_plan.http', 'w') as self.app.file_obj:
            response = self.app.get('/plans/{}'.format(plan_id))

        with open(TARGET_DIR + 'plan-listing.http', 'w') as self.app.file_obj:
            self.app.authorization = None
            response = self.app.get('/plans')
            self.assertEqual(response.status, '200 OK')
            self.app.file_obj.write("\n")

        self.app.authorization = ('Basic', ('broker', ''))
        with open(TARGET_DIR + 'patch-plan-procuringEntity-name.http', 'w') as self.app.file_obj:
            response = self.app.patch_json(
                '/plans/{}?acc_token={}'.format(plan['id'], owner_token),
                {'data':
                    {"items": [
                        {
                            "description": "Насіння овочевих культур",
                            "classification": {
                                "scheme": "ДК021",
                                "description": "Vegetable seeds",
                                "id": "03111700-9"
                            },
                            "additionalClassifications": [
                                {
                                    "scheme": "ДКПП",
                                    "id": "01.13.6",
                                    "description": "Насіння овочевих культур"
                                }
                            ],
                            "deliveryDate": {
                                "endDate": "2016-06-01T23:06:30.023018+03:00"
                            },
                            "unit": {
                                "code": "KGM",
                                "name": "кг"
                            },
                            "quantity": 5000
                        }
                    ]}
                })

        with open(TARGET_DIR + 'plan-listing-after-patch.http', 'w') as self.app.file_obj:
            self.app.authorization = None
            response = self.app.get('/plans')
            self.assertEqual(response.status, '200 OK')
            self.app.file_obj.write("\n")
