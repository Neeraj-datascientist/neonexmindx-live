const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Testing actual click action on WhatsApp elements...');
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });

  // Test click on Floating WhatsApp Button
  const floatWa = page.locator('.site-floating-whatsapp');
  try {
    const [popup] = await Promise.all([
      context.waitForEvent('page', { timeout: 3000 }).catch(() => null),
      floatWa.click()
    ]);
    console.log('Click on .site-floating-whatsapp succeeded! Popup opened:', !!popup);
    if (popup) {
      console.log('Popup URL:', popup.url());
      await popup.close();
    }
  } catch (err) {
    console.error('Click error on .site-floating-whatsapp:', err.message);
  }

  // Switch to mobile viewport and test .mobile-actions a.btn-primary
  await page.setViewportSize({ width: 375, height: 667 });
  const mobileWa = page.locator('.mobile-actions a.btn.btn-primary');
  try {
    const [popupMobile] = await Promise.all([
      context.waitForEvent('page', { timeout: 3000 }).catch(() => null),
      mobileWa.click()
    ]);
    console.log('Click on .mobile-actions a.btn.btn-primary succeeded! Popup opened:', !!popupMobile);
    if (popupMobile) {
      console.log('Mobile Popup URL:', popupMobile.url());
      await popupMobile.close();
    }
  } catch (err) {
    console.error('Click error on .mobile-actions WhatsApp:', err.message);
  }

  await browser.close();
})();
