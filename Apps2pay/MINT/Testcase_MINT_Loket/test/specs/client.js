const {remote} = require('webdriverio')
const {config} = require ('../../wdio.conf.js')

const capabilities = config.capabilities[0]

const wdOpts = {
    hostname : '127.0.0.1',
    port : 4724,
    logLevel: 'info',
    capabilities:capabilities,
}

let client;

async function initClient () {
    if (!client){
        client = await remote(wdOpts)
    } 
    return client
}

async function deleteClient () {
    if (client) {
        await client.deleteSession()
    }
}

module.exports = {initClient, deleteClient}