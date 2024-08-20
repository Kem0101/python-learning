from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# con estas dos lineas de codigo podemos hacer que la paginas o aplicacion que vamos a testear en el navegador permanezca abierta
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("https://github.com")
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()


user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys("kem0101")
pass_input.send_keys("Dioswithme16")
pass_input.send_keys(Keys.RETURN)

# de esta forma puedo verificar que valor contiene el elemento con clase truncate-text(especificamente esta verificando el nombre de usuario), deberiamos verificar por alguna propiedad que sea unica del elemento
profile = browser.find_element(By.CLASS_NAME, "Truncate-text")
label = profile.get_attribute("innerHTML")
# print(label)

# de esta forma lanzamos un exception para verificar si existe este nombre de usuario en dicho elemento
assert "Kem0101" in label

# cerrar el navegador el ejecutar todo el script, debemos eliminar el metodo chromeoption
browser.quit()
