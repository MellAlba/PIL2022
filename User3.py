#User3
#Base para todo 

  
import time 

from selenium import webdriver 

from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.by import By 

 
 

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe") 

driver.get("https://www.bensimon.com.ar/") 

time.sleep(3) 

previous_tabs = set(driver.window_handles) 

previous_tab = driver.current_window_handle 

 
 

#TEST CASE 642 

 
 

linkCierrePopUp = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[1]/div[2]/button") 

time.sleep(2) 

linkCierrePopUp.click() 

time.sleep(2) 

 
 

linkHome = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[1]/div") 

time.sleep(2) 

linkHome.click() 

time.sleep(2) 

 
 

if driver.current_url == "https://www.bensimon.com.ar/": 

        print("Estoy en la URL correcta - Home") 

 
 

#TEST CASE 643 

 
 

coleccion = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[2]/div/div/div/div/div/div/div/nav/ul/li[5]/div") 

time.sleep(1) 

coleccion.click() 

time.sleep(2) 

 
 

if driver.current_url == "https://www.bensimon.com.ar/coleccion?order=OrderByReleaseDateDESC": 

        print("Estoy en la URL correcta - Coleccion") 

time.sleep(2) 

 
 

linkVolver = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[3]/div/div/section/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/a") 

if linkVolver != 0: 

  print("Existe el elemento Volver") 

time.sleep(2) 

 
 

linkHome = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[1]/div") 

time.sleep(2) 

linkHome.click() 

time.sleep(2) 

 
 

linkStories = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[2]/div/div/div/div/div/div/div/nav/ul/li[7]") 

time.sleep(2) 

linkStories.click() 

time.sleep(2) 

 
 

if driver.find_element == (By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[2]/div/div/div/div/div/div/div/nav/ul/li[7]/div[2]/div/section/div/div/div/div/div/div/div/div/nav/ul/li[1]/div/a/div"): 

        print("La subsección de Stories llamada TOUR DE LA VILLE es un vínculo") 

time.sleep(2) 

 
 

linkTOURDELAVILLE = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[2]/div/div/div/div/div/div/div/nav/ul/li[7]/div[2]/div/section/div/div/div/div/div/div/div/div/nav/ul/li[1]/div/a/div") 

time.sleep(2) 

linkTOURDELAVILLE.click() 

time.sleep(2) 

 
 

if driver.current_url == "https://www.bensimon.com.ar/tourdelaville": 

        print("Estoy en la URL correcta - TOUR DE LA VILLE") 

time.sleep(2) 

 
 

linkHome = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[1]/div") 

time.sleep(2) 

linkHome.click() 

time.sleep(2) 

 
 

#TEST CASE 644 

 
 

if driver.find_element == (By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/label/div/input"): 

        print("Existe un cuadro de búsqueda contíguo al ícono de búsqueda") 

time.sleep(2) 

 
 

inputBilletera = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/label/div/input") 

inputBilletera.send_keys('Billetera') 

inputBilletera.send_keys(Keys.ENTER) 

time.sleep(3) 

 
 

if driver.current_url == "https://www.bensimon.com.ar/billetera?_q=billetera&map=ft": 

        print("Escribí correctamente Billetera") 

time.sleep(2) 

 
 

linkHome = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[1]/div") 

time.sleep(2) 

linkHome.click() 

time.sleep(2) 

 
 

if driver.find_element == (By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[3]/a"): 

        print("Existe el vínculo de localización") 

time.sleep(2) 

 
 

linkUbicacion = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[3]") 

time.sleep(2) 

linkUbicacion.click() 

time.sleep(2) 

 
 

newWindow = (set(driver.window_handles) - previous_tabs).pop() 

driver.switch_to.window(newWindow) 

time.sleep(3) 

driver.close() 

driver.switch_to.window(previous_tab) 

time.sleep(3) 

 
 

if driver.find_element == (By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[4]/a"): 

        print("Existe el vínculo de favoritos") 

time.sleep(2) 

 
 

linkFavoritos = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[4]/a") 

time.sleep(2) 

linkFavoritos.click() 

time.sleep(2) 

 
 

if driver.current_url == "https://www.bensimon.com.ar/login?returnUrl=/login": 

        print("La URL de redirección es la correcta para loguearse") 

time.sleep(2) 

 
 

linkHome = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[1]/div") 

time.sleep(2) 

linkHome.click() 

time.sleep(2) 

 
 

linkIngresar = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[5]") 

time.sleep(2) 

linkIngresar.click() 

time.sleep(2) 

 
 

linkEntrarenIngresar = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[2]/div/button/div") 

time.sleep(2) 

linkEntrarenIngresar.click() 

time.sleep(2) 

 
 

linkVolverEnEntrar = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div[1]/button/div") 

time.sleep(2) 

linkVolverEnEntrar.click() 

time.sleep(1) 

 
 

linkBolsa = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[6]") 

time.sleep(2) 

linkBolsa.click() 

time.sleep(2) 

 
 

if driver.find_element == (By.XPATH,"/html/body/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div"): 

        print("Sí existe el texto La bolsa está vacía") 

time.sleep(2) 


driver.close() 
