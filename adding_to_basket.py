{
  "id": "a2964446-a503-41f2-8721-f985dcaa89c1",
  "version": "1.1",
  "name": "1",
  "url": "https://orchardmile.com",
  "tests": [{
    "id": "127a9bd3-a2e2-4224-a69b-9f59d4016ffd",
    "name": "1",
    "commands": [{
      "id": "d581b947-a1fd-40ff-a0f3-d3f06b71b29c",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "15413a84-b0e1-4e8d-ba75-6e5d73d0660c",
      "comment": "",
      "command": "click",
      "target": "css=a.login-btn",
      "targets": [
        ["css=a.login-btn", "css"],
        ["xpath=//a[contains(text(),'Sign\n              In')]", "xpath:link"],
        ["xpath=//div[@id='ssh1']/header/div/div/div[3]/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'javascript:void(0);')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "71eda786-bd88-499b-a9c5-7d975b06a547",
      "comment": "",
      "command": "type",
      "target": "xpath=(//input[@name='email'])[2]",
      "targets": [
        ["xpath=(//input[@name='email'])[2]", "xpath:attributes"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "test@mailinator.com"
    }, {
      "id": "3675dabd-0cdb-4217-9a46-51fb124bd027",
      "comment": "",
      "command": "type",
      "target": "name=password",
      "targets": [
        ["name=password", "name"],
        ["css=input[name=\"password\"]", "css"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": "12345QwE"
    }, {
      "id": "546d5007-f280-4293-9c11-38c3cec574b9",
      "comment": "",
      "command": "mouseDownAt",
      "target": "xpath=(//input[@name='email'])[2]",
      "targets": [
        ["xpath=(//input[@name='email'])[2]", "xpath:attributes"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "-23,35.08332824707031"
    }, {
      "id": "ccd422c5-9c29-441e-a667-dd055e335dc0",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "xpath=(//input[@name='email'])[2]",
      "targets": [
        ["xpath=(//input[@name='email'])[2]", "xpath:attributes"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "-23,35.08332824707031"
    }, {
      "id": "1f6c7e9a-697d-452b-ae15-da85e541cf92",
      "comment": "",
      "command": "mouseUpAt",
      "target": "xpath=(//input[@name='email'])[2]",
      "targets": [
        ["xpath=(//input[@name='email'])[2]", "xpath:attributes"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "-23,35.08332824707031"
    }, {
      "id": "19db6f23-4629-4f45-9ca6-16b72e9f5059",
      "comment": "",
      "command": "click",
      "target": "xpath=(//input[@name='email'])[2]",
      "targets": [
        ["xpath=(//input[@name='email'])[2]", "xpath:attributes"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "394e5c00-07cf-48ad-9518-7ca36d89d5bc",
      "comment": "",
      "command": "click",
      "target": "css=button[type=\"submit\"]",
      "targets": [
        ["css=button[type=\"submit\"]", "css"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[3]/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2a4f5a2f-66a8-4408-b4f5-adb92d9a8d62",
      "comment": "",
      "command": "mouseOver",
      "target": "css=div.home-left",
      "targets": [
        ["css=div.home-left", "css"],
        ["xpath=//section[@id='main']/div[2]/div/div/div/div/homepage-tiles/div/div/div/a/div", "xpath:idRelative"],
        ["xpath=//homepage-tiles/div/div/div/a/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "3f2f8782-ae6c-44a4-850c-d8da2f9444a2",
      "comment": "",
      "command": "mouseOut",
      "target": "css=div.home-left",
      "targets": [
        ["css=div.home-left", "css"],
        ["xpath=//section[@id='main']/div[2]/div/div/div/div/homepage-tiles/div/div/div/a/div", "xpath:idRelative"],
        ["xpath=//homepage-tiles/div/div/div/a/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9d378e07-9f38-4974-ae92-a9444b51babe",
      "comment": "",
      "command": "click",
      "target": "xpath=//a[contains(text(),'accessories')]",
      "targets": [
        ["xpath=//a[contains(text(),'accessories')]", "xpath:link"],
        ["xpath=//div[@id='ssh1']/header/div/div[2]/ul/li[6]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/accessories')]", "xpath:href"],
        ["xpath=//div[2]/ul/li[6]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4dc89a67-07db-4945-8566-800fb390be30",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,0)",
      "targets": [],
      "value": ""
    }, {
      "id": "6e5cfd36-a05d-4e4b-8d70-11b7f8f8e293",
      "comment": "",
      "command": "mouseOver",
      "target": "xpath=//a[contains(text(),'shoes')]",
      "targets": [
        ["xpath=//a[contains(text(),'shoes')]", "xpath:link"],
        ["xpath=//div[@id='ssh1']/header/div/div[2]/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/shoes')]", "xpath:href"],
        ["xpath=//div[2]/ul/li[4]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "614c4c49-74da-4b1d-8157-bade62004330",
      "comment": "",
      "command": "click",
      "target": "css=span.product-brand",
      "targets": [
        ["css=span.product-brand", "css"],
        ["xpath=//section[@id='main']/div[2]/div/div[3]/div[2]/div/product-list/div/transclude/div/product-list-items/div/div/transclude/product-list-item/div/a/div/span", "xpath:idRelative"],
        ["xpath=//div/a/div/span", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6c9a6a1d-0869-4b9c-adb8-17e62c0c4c8d",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,0)",
      "targets": [],
      "value": ""
    }, {
      "id": "0da609ff-e3d4-4fe7-81d6-2f7401cd6a6b",
      "comment": "",
      "command": "click",
      "target": "css=button.btn-add-to-cart",
      "targets": [
        ["css=button.btn-add-to-cart", "css"],
        ["xpath=//section[@id='main']/div[2]/div/div/div[2]/div[6]/div/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2728a4c5-1611-41e0-a72b-f13ed6468175",
      "comment": "",
      "command": "mouseOver",
      "target": "css=button.close-btn",
      "targets": [
        ["css=button.close-btn", "css"],
        ["xpath=//body/div/div/div/div[2]/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eef823ef-8628-4588-a67d-565d838259b8",
      "comment": "",
      "command": "click",
      "target": "css=button.close-btn",
      "targets": [
        ["css=button.close-btn", "css"],
        ["xpath=//body/div/div/div/div[2]/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ef94b9ab-74c6-4c42-99bf-f7457cb4d7d4",
      "comment": "",
      "command": "mouseOut",
      "target": "css=button.close-btn",
      "targets": [
        ["css=button.close-btn", "css"],
        ["xpath=//body/div/div/div/div[2]/button", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "a7bf2f99-c616-419a-83dc-d720d5c3e10e",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["127a9bd3-a2e2-4224-a69b-9f59d4016ffd"]
  }],
  "urls": ["https://orchardmile.com/"],
  "plugins": []
}