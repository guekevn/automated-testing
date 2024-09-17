const loginPage = require('../pageobjects/login/login.page');

describe('Login Aplikasi LMS', () => {
    it('Login berhasil', async () => {
        await loginPage.login('00031', 'adminkevin2', '999999')
    })
})