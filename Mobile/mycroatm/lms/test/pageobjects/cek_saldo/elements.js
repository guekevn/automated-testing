class cekSaldoElements {
    get menuCekSaldo () {
        return $('android= new UiSelector().text("Cek Saldo")')
    }

    get buttonCekSaldo () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btnCekSekarang")')
    }

    get buttonRekeningTabungan () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btn_tabungan")')
    }

    get buttonRekeningGiro () {
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btn_giro")')
    }

    get insertCardPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonCancelTransaction (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/btl_transaksi")')
    }

    get inputPINPage (){
        return $('android= new UiSelector().resourceId("com.whty.tysecuritypin:id/keyboard_view")')
    }

    get successPage (){
        return $('android= new UiSelector().resourceId("android:id/content")')
    }

    get buttonReprintCekSaldo (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linPrintSaldo")')
    }

    get buttonSelesaiCekSaldo (){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/linSelesaiSaldo")')
    }
}

module.exports = new cekSaldoElements()