import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
	await page.goto('/');
	await expect(page).toHaveTitle(/PrepAI/);
	await page.locator('textarea[id="text-input"]').click();
	await page.locator('textarea[id="text-input"]').fill('The mitochondria is the powerhouse of the cell.');
	await page.getByRole('button', { name: 'Generate Quiz' }).click();
	await expect(page.getByRole('heading', { name: 'Question 1 of 3' })).toBeVisible();
	await page.screenshot({ path: '/home/swebot/jules-scratch/verification/verification.png' });
});
