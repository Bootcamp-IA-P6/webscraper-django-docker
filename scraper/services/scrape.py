import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

def run_scraper():
    options = Options()
    options.add_argument("--headless")
    resultados = [] 

    driver = webdriver.Remote(
        command_executor='http://firefox:4444/wd/hub',
        options=options
    )

    try:
        # Usamos una web de startups real
        url = "https://remoteok.com/remote-startup-jobs"
        driver.get(url)
        
        # Esperamos un par de segundos a que cargue el contenido dinámico
        driver.implicitly_wait(5)
        
        # --- CAPTURA DE PANTALLA ---
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"captura_{timestamp}.png"
        ruta_captura = os.path.join('/app/screenshots', nombre_archivo)
        driver.save_screenshot(ruta_captura)
        print(f"📸 Captura guardada en: {ruta_captura}")
        
        # --- EXTRACCIÓN DE DATOS ---
        # En RemoteOK, los títulos suelen estar en h2 con la clase 'item' o similar
        # Vamos a probar con un selector genérico de títulos de trabajo
        elementos = driver.find_elements(By.CSS_SELECTOR, "h2")
        
        for el in elementos:
            titulo = el.text.strip()
            if titulo:
                resultados.append({
                    'title': titulo,
                    'url': url
                })
        
        print(f"✅ Se han encontrado {len(resultados)} ofertas de trabajo.")

    except Exception as e:
        print(f"❌ Error durante el scraping: {e}")
    
    finally:
        driver.quit()
        return resultados