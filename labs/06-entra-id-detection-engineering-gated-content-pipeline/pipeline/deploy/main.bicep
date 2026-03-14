@description('Target Log Analytics workspace resource ID used as the workbook sourceId.')
param workspaceResourceId string

@description('Azure location for extension resources that require it.')
param location string = resourceGroup().location

@description('Optional workbook display name override.')
param workbookDisplayName string = 'Lab06 Identity Detection Dashboard'

var workbookDefinition = loadJsonContent('workbook.serialized.json')
var workbookSerialized = replace(string(workbookDefinition.serializedData), '{WORKSPACE_RESOURCE_ID}', workspaceResourceId)

resource deployableWorkbook 'Microsoft.Insights/workbooks@2023-06-01' = {
  name: guid(resourceGroup().id, workbookDisplayName, 'lab06-workbook')
  location: location
  kind: 'shared'
  properties: {
    displayName: workbookDisplayName
    category: workbookDefinition.category
    sourceId: workspaceResourceId
    version: workbookDefinition.version
    serializedData: workbookSerialized
  }
}

output workbookResourceId string = deployableWorkbook.id
output workbookName string = deployableWorkbook.name
output workbookSourceId string = workspaceResourceId
