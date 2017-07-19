# Create a Protocol

To create a **protocol**.

Follow the initialization steps：
1. Create a protocol.
2. .....

## Method

`POST        /protocols`


### Parameters

| Parameter | Description | Example | Required | Remark |
| --------- | ----------- | ------- | -------- | -------|
| schema_name | schema name | as66kbsa | Required | Condition: [a-z0-9], Auto generated |
| title |  Protocol Title | 評估以LY2951742治療陣發性偏頭痛病患的一項第3期、隨機分配、雙盲、安慰劑對照試驗－ EVOLVE-2試驗 | Required | |
| display_name | Protocol Display Name | 評估以LY2951742治療陣發性偏頭痛病患的一項第3期 | optional | |
| purpose | Research purpose | 檢驗假說：用於陣發性偏頭痛病患時，至少1種劑量之LY2951742 (120或240 mg/month)預防偏頭痛的效果優於安慰劑。 | Required | |
| indications | Indications | 陣發性偏頭痛 | Required | |
| icd | ICD 10 | M27.3 | Required | |
| type | 0: PI Initiate, 1: hospital, 2: sponsor | 1 | Required | |
| site | if type is hospital, please full this field | 台北榮總 | Required | |
| sponsor | if type is sponsor, please full this field | 
| apply_number | protocol apply number | I5Q-MC-ACHY | optional | |
| approval_number | Approval Number | I5AR9877 | optional | |
| approval_date | Approval Date | 2017-07-18T08:44:11.175369 | optional | ISO 8601 format |
| serial_number | protocol serial number | I5Q-MC-CGAH | optional | |
| phase | Protocol Phase | III | optional | |
| estimate_period_start | Estimate Period start | 2017-07-18T08:57:40.845352 | optional | ISO 8601 format |
| estimate_period_end | Estimate Period end | 2018-07-18T08:57:40.845352 | optional | ISO 8601 format |
| center_type | category | Single Center or Multicenter | Required | |
| principal_investigator |  principal investigator |  | Required | Required | |
| protocol_manager | protocol owner |  | Required | Required | |

### Request / Response

```bash
# Request
curl -H "Content-Type: application/json" \
-X POST -d '{
    "title": "評估以LY2951742治療陣發性偏頭痛病患的一項第3期、隨機分配、雙盲、安慰劑對照試驗－ EVOLVE-2試驗",
    "display_name": "評估以LY2951742治療陣發性偏頭痛病患的一項第3期",
    "purpose": "檢驗假說：用於陣發性偏頭痛病患時，至少1種劑量之LY2951742 (120或240 mg/month)預防偏頭痛的效果優於安慰劑。",
    

}' https://app.sydney.com/protocols 
-d "owner=as66kbsa" \
-d "name=評估以LY2951742治療陣發性偏頭痛病患的一項第3期、隨機分配、雙盲、安慰劑對照試驗－ EVOLVE-2試驗"\
-d "approval_date=2016/02/01" \
-d "start_date=2016/02/01" \
-d "end_date=2018/06/17" \
-d "examine_number=I5AR9877" \
-d "protocol_number=I5Q-MC-CGAH" \
-d "purpose=檢驗假說：用於陣發性偏頭痛病患時，至少1種劑量之LY2951742 (120或240 mg/month)預防偏頭痛的效果優於安慰劑。"\
-d "indications=陣發性偏頭痛" \
-d "category=Multicenter" \
-d "type=藥品查驗登記" \
-d "phase=III" 

# Response
HTTP/1.1 201
{
  "data": {
    "type": "protocol",
    "id": "di98kbsa",
    "attributes": {
      "owner": "as66kbsa",
      "name": "評估以LY2951742治療陣發性偏頭痛病患的一項第3期、隨機分配、雙盲、安慰劑對照試驗－ EVOLVE-2試驗",
      "approval_date": "2016/02/01",
      "start_date": "2016/02/01",
      "end_date": "2018/06/17",
      "examine_number": "I5AR9877",
      "protocol_number": "I5Q-MC-CGAH",
      "purpose": "檢驗假說：用於陣發性偏頭痛病患時，至少1種劑量之LY2951742 (120或240 mg/month)預防偏頭痛的效果優於安慰劑。",
      "indications": "陣發性偏頭痛",
      "category": "Multicenter",
      "type": "藥品查驗登記",
      "phase": "III",
      "created_at": "2016-04-06T04:11:48.951Z",
      "updated_at": "2016-04-06T04:11:48.951Z"
    },
    "relationships": {
      "members": {
        "data": [
          { "type": "members", "id": "as66kbsa" },
          { "type": "members", "id": "ddd3kbsa" }
        ],
        "links": {
          "self": "https://app.sydney.com/api/v1/protocols/di98kbsa/members"
        }
      }
    }
  },
  "links": {
    "self": "https://app.sydney.com/api/v1/protocols/dHJH78ab"
  }
}
```

### Errors

```bash
# Response
HTTP/1.1 400

{
  "errors": [
    {
      "code": 101,
      "type": "TokenExpired",
      "title": "Token had expired",
      "detail": "Romote token does not match with local token."
    }
  ]
}
```

### Fake Data

```bash
curl -H "Authorization: CRrppi1DELemyXr83szSnahV" \
https://app.sydney.com/api/v1/protocols \
-d "owner=as66kbsa" \
-d "name=A Phase II study of the combination of Erlotinib and Bevacizumab in patients with Advanced or Metastatic Hepatocellular Carcinoma (HCC)"\
-d "approval_date=2007/11/01" \
-d "start_date=2007/11/01" \
-d "end_date=2011/12/31" \
-d "examine_number=M34T678" \
-d "protocol_number=MLIQ-M2C-FGA1" \
-d "purpose=在第16週時評估無病存活率(Progression-free survival rate)次要目標:根據整體反應率(overall response rate)、疾病控制率(disease control rate)、腫瘤惡化時間(time to tumour progression)、無病存活(progression-free survival)及整體存活(overall survival)進一步評估療效。"\
-d "indications=侵襲性肝細胞癌" \
-d "category=Single Center" \
-d "type=前瞻性研究" \
-d "phase=III" 

curl -H "Authorization: CRrppi1DELemyXr83szSnahV" \
https://app.sydney.com/api/v1/protocols \
-d "owner=as66kbsa" \
-d "name=A randomized double blind placebo controlled study evaluating the glycemic effect of rimonabant added to metformin in patients with type 2 diabetes insufficiently controlled with metformin monotherapy"\
-d "approval_date=2008/03/01" \
-d "start_date=2008/03/01" \
-d "end_date=2010/12/31" \
-d "examine_number=EG89K908" \
-d "protocol_number=AIQ-C2C-R2GA" \
-d "purpose=檢驗假說：評估在47週期間併用rimonabant和metformin的安全性。"\
-d "indications=第二型糖尿病" \
-d "category=Single Center" \
-d "type=前瞻性研究" \
-d "phase=II" 
```
