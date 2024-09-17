const historyPage = require('../pageobjects/history.page')

describe('History Aplikasi LMS', () => {
    it('Menu history berjalan dengan sesuai', async () => {
        await historyPage.history()
    })
})