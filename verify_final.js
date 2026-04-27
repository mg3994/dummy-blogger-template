const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Set viewport for desktop
  await page.setViewportSize({ width: 1280, height: 800 });

  // Load the rendered HTML
  const filePath = `file://${process.cwd()}/final_render.html`;
  await page.goto(filePath);

  // Verify Header Links
  const signInBtn = await page.$('a.btn[href="https://dash.antinna.in"]');
  console.log('Sign In button found:', !!signInBtn);

  // Test Theme Toggle (3-mode)
  const getTheme = () => page.evaluate(() => document.documentElement.getAttribute('data-user-color-scheme'));
  const getActiveTheme = () => page.evaluate(() => document.documentElement.getAttribute('data-theme'));

  console.log('Initial mode:', await getTheme());

  await page.click('#theme-toggle');
  console.log('Mode after 1 click:', await getTheme()); // Should be light

  await page.click('#theme-toggle');
  console.log('Mode after 2 clicks:', await getTheme()); // Should be dark

  await page.click('#theme-toggle');
  console.log('Mode after 3 clicks:', await getTheme()); // Should be system

  // Take screenshots
  await page.screenshot({ path: 'final_desktop.png', fullPage: true });

  // Mobile check
  await page.setViewportSize({ width: 375, height: 812 });
  await page.screenshot({ path: 'final_mobile.png' });

  await browser.close();
})();
