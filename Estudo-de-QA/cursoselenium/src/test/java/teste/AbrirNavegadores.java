package teste;

import static org.junit.Assert.fail;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


public class AbrirNavegadores {
	
	
	// Instanciando a Classe WebDriver
	static WebDriver driver;
	
	@BeforeClass // Roda antes dos testes
	public static void setUpBeforeClass() throws Exception {
		// Informando onde está o executável dos navegadores
		//System.setProperty("webdriver.chrome.driver","../../webdrivers/chromedriver");
		 System.setProperty("webdriver.gecko.driver","../../webdrivers/geckodriver");
		
		// Instanciando os navegadores
		 driver = new FirefoxDriver();
		// driver = new ChromeDriver();
		
		// página a ser aberta como teste.
		driver.get("https://www.youtube.com");
		
	}
	
	@Test
	public void test() {
		fail("Not yet implemented");
	}

	@AfterClass // Roda após os testes
	public static void tearDownAfterClass() throws Exception {
		// Este fecha somente a aba usada.
		driver.close();
		
		// Esta fecha todo o Browser
		//driver.quit();
	}

	//
	//@Before
	//public void setUp() throws Exception {
	//}
//
	//@After
	//public void tearDown() throws Exception {
	//}

	

}
