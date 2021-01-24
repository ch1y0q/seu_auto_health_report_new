# 东南大学每日打卡（新版）

使用Selenium库编写的东南大学每日打卡脚本。

## Requirements

* Python 3

* Selenium

* webdriver that corresponds to your browser (I use chrome thus /webdriver/chromedriver.exe, you may need to download webdriver of your own browser and modify code a little bit)

# Features

Log in with designated username and password.

Navigate to daily health report and automatically click "new".

Randomly generate a body temperature between 36.2 to 37.0 and fill the field.

Submit.

## Usage

`python auto_report.py USERNAME PASSWORD`

OR

`python auto_report.py USERNAME PASSWORD[BASE64 DECODED] 1`



If you wish to run the script automatically at a certain time of a day, consider using task scheduler (on Windows).



## Disclaimer

TL;DR: I  DON'T CARE ABOUT WAHT YOU DO WITH THE CODE, BUT IF YOU DID DO SOMETHING AND GOT CAUGHT, IT IS YOU AND ONLY YOU TO BE RESPONSIBLE.

THE CODE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) SUSTAINED BY YOU OR A THIRD PARTY, HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT ARISING IN ANY WAY OUT OF THE USE OF THIS SAMPLE CODE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.