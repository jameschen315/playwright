Playwright is an open-source Node.js library that enables developers to automate web browsers. It was developed by Microsoft and is now maintained by a community of contributors. Playwright provides a high-level API for automating browsers, including Chromium, Firefox, and WebKit, across multiple operating systems. It allows developers to write reliable and maintainable browser automation scripts that can be used for testing, scraping, and other web automation tasks.

Some of the key features of Playwright include:
Cross-browser support: Playwright supports Chromium, Firefox, and WebKit, which covers a large percentage of the desktop and mobile browser market.
Multi-language support: Playwright supports multiple programming languages, including Node.js, Python, and .NET.
High-level API: Playwright provides a high-level. 
Playwright is very fast because it uses Browser Projects unlike Selenium which use full Browsers. Playwright has build-in wait.
https://playwright.dev/python/docs/intro

This is my first 'Page Object' model automation with PlayWright.

Instruction to make your first Playwright test with Pytest and Python:
1. I recommended download all the packages in virtual environment
  python3 -m venv venv
2. activate source
  source venv/bin/activate
3. Install Playwright
  pip3 install playwright
4. Install Pytest
  pip3 install pytest
5. Install Playwright pytest plugin
  a. pip3 install pytest-playwright
6. Check the plugin installed in your virtual environment
  pip3 freeze
7. I recommended Mircosoft Visual studio code ide
  https://code.visualstudio.com/
8. Run your test in command line
  python3 -m pytest test/my_first_test.py -> headless
  python3 -m pytest test/my_first_test.py --headed --slowmo 1000 -> with default Chromium browser project and with 1 sec wait
  python3 -m pytest test/my_first_test.py --headed --slowmo 1000 --browser firefox -> specific with Firefox browser project
  python3 -m pytest test/my_first_test.py --headed --slowmo 1000 --browser firefox --browser chromium -> multiple browsers
  python3 -m pytest tests/my_first_test.py --browser chromium --device="iPhone 13"  --headed --slowmo 1000 -> run test in device emulator
 9. Run your test parallel
  pip3 install pytest-xdist
 10. Run test parallel on 3 browsers
  python3 -m pytest test/my_first_test.py --headed --slowmo 1000 -n2 --browser firefox --browser chromium --browser webkit
 11. Playwright allow you to run stack browsers with argument "--browser-channel chrome" - you need to have the browser installed
  python3 -m pytest test/my_first_test.py --headed --slowmo 1000 --browser-channel chrome 


  
  
