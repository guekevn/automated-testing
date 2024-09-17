class loginElements {
    get CIDField(){
        return $('android= new UiSelector().text("CID")')
    }
    get UsernameField(){
        return $('android= new UiSelector().text("Username")')
    }
    get PasswordField(){
        return $('android= new UiSelector().text("Password")')
    }

    get ButtonSubmit(){
        return $('android= new UiSelector().text("Masuk")')
    }

    get homePage(){
        return $('android= new UiSelector().resourceId("com.mycroatm.lsm:id/action_bar_root")')
    }
}

module.exports = new loginElements()