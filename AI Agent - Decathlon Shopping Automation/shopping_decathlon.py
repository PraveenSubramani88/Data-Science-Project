from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig 
from dotenv import load_dotenv
load_dotenv()

import asyncio

task="""
  🏊 Prompt for Shopping Agent : Decathlon Order
Objective:
Visit Decathlon India, search for the required sports items, add them to the cart with the correct sizes, and verify the cart before checkout.

🟡 Step 1: Navigate to the Website
Open Decathlon India.
Ensure the homepage fully loads.
Close any pop-ups (location, newsletters) by clicking the “X” if they appear.
Accept cookies if prompted.
🛒 Step 2: Add Items to the Cart
🎯 Shopping List:
Adult Swimming Goggles
Search: "Adult Swimming Goggles Men Women UV Protection Soft 100 Tinted Lenses Black Blue"
Select the exact match from results.
Verify the product title matches.
Click “Add to Cart”.
Adult Swimming Cap
Search: "Adult Swimming Cap Silicone Mesh 56-60 Cm Print Yellow Expe"
Confirm size range: 56-60 cm from product details.
Add to cart.
Men’s Surfing Long Sleeve UV Protection (UPF50+) Blue
Search: "Men Surfing Long sleeve UV Protection (UPF50+) Blue"
Select Size: M (Medium).
Add to cart.
Men’s Swimming Shorts – Jammer 100 Basic Black
Search: "Men's swimming shorts - Jammer 100 basic black"
Select Size: M (Medium).
Add to cart.
✅ Step 3: Verify Items in Cart
Open the cart page (usually the cart icon at the top-right).
Confirm that the 4 items are present with the correct sizes for items 3 and 4.
Check that only 1 unit of each item is added.
⚠️ Step 4: Handling Errors or Unavailable Items
If an item is out of stock, search for a similar item with the same features (e.g., goggles with UV protection and tinted lenses).
If multiple options match, select the highest-rated or best-reviewed product.
If the size M is out of stock for items 3 or 4, choose Size L as an alternative.
Log any substitutions made.
🛒 Step 5: Adjusting for Minimum Cart Value (if applicable)
If the total cart value is below any minimum for free shipping, add a low-cost swimming accessory (e.g., earplugs or nose clips).
Do NOT add more than one additional item unless necessary.
💳 Step 6: Proceed to Checkout (Optional)
Proceed to the checkout page.
Stop at payment unless instructed to complete it.
📝 Step 7: Output Summary
Provide a summary of the order:
✅ Items Purchased: List names, sizes, and any substitutions.
💰 Total Cart Value:
🔄 Substitutions Made (if any):
🚫 Items Skipped (if unavailable):
💡 Important Guidelines for the Agent:
Be precise in item selection (use exact search terms).
Do not add extras unless necessary for cart value minimum.
Select size “M” only for items 3 and 4.
Use best alternatives if items are unavailable.
One unit per item only.
"""

browser = Browser()

agent = Agent(
   task=task,
    llm=    ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key='your_api_key'),
    browser=browser,
    )

async def main():
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
