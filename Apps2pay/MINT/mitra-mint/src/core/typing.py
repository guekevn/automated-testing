from appium.webdriver.extensions.android.nativekey import AndroidNativeKey

DIGIT_KEYCODE = {
    "0": AndroidNativeKey.DIGIT_0,
    "1": AndroidNativeKey.DIGIT_1,
    "2": AndroidNativeKey.DIGIT_2,
    "3": AndroidNativeKey.DIGIT_3,
    "4": AndroidNativeKey.DIGIT_4,
    "5": AndroidNativeKey.DIGIT_5,
    "6": AndroidNativeKey.DIGIT_6,
    "7": AndroidNativeKey.DIGIT_7,
    "8": AndroidNativeKey.DIGIT_8,
    "9": AndroidNativeKey.DIGIT_9,  
}

def type_via_keyevents(driver, element, text: str):
    element.click()  # fokus ke element
    for ch in text:
        driver.press_keycode(DIGIT_KEYCODE[ch])