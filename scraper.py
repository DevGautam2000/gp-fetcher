import json
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
}


session = requests.Session()  # create a session

def saveAsForked(name, src, about, tech_stacks, license_, from_):
    forked[name] = {
        "src": src,
        "about": about,
        "tech-stack": tech_stacks,
        "license": license_,
        "from": from_

    }


def save(name, src, about, tech_stacks, license_):
    projectInfo[name] = {
        "src": src,
        "about": about,
        "tech-stack": tech_stacks,
        "license": license_

    }


def handle_pagination(username, url):
    errors = []
    
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    for div in soup.findAll("div", id="user-repositories-list"):
        for li in div.select('ul>li'):
            inner_soup = BeautifulSoup(str(li), "lxml")
            tech_stacks = []
            license_ = ""
            name = ""
            about = ""
            from_ = ""
            src = f"https://github.com/{li.a['href']}"

            # if li.a.text.strip() != username:
            try:
                name = inner_soup.find(
                    attrs={"itemprop": "name codeRepository"}).text.strip()
            except Exception as e:
                errors.append(e)
            try:
                about = inner_soup.find(
                    attrs={"itemprop": "description"}).text.strip()
            except Exception as e:
                errors.append(e)
            try:
                tech_stacks.append(inner_soup.find(
                    attrs={"itemprop": "programmingLanguage"}).text.strip())
            except Exception as e:
                errors.append(e)
            try:
                if li.select('span')[len(li.select('span')) - 1]['class'][0] == 'mr-3':
                    license_ = li.select('span')[len(
                        li.select('span')) - 1].text.strip()

                if "Template" == li.span.text.strip():
                    license_ = li.select("span")[5].text.strip()

            except Exception as e:
                errors.append(e)
            try:

                if "Forked" in li.span.text.strip():
                    from_ = li.span.text.strip()

                if "Template" == li.span.text.strip():
                    from_ = li.select("span")[1].text.strip()

            except Exception as e:
                errors.append(e)

            try:
                if "Forked" in li.span.text.strip() or li.span.text.strip() == "Template":
                    saveAsForked(name, src, about,
                                 tech_stacks, license_, from_)
                else:
                    save(name, src, about, tech_stacks, license_)

            except Exception as e:
                errors.append(e)
                save(name, src, about, tech_stacks, license_)
    try:
        if soup.find(attrs={"data-test-selector": "pagination"}):
            div = soup.find(
                attrs={"data-test-selector": "pagination"}).select("a")

            for a in div:
                if a.text == "Next":
                    url = a['href']
            errors.clear()
            handle_pagination(username, url)
    except Exception as e:
        errors.append(e)



def scrape(_username):
    global projectInfo
    projectInfo = {}
    global forked
    forked = {}
    fileName = f"{_username}-projects"
    first_url = f"https://github.com/{_username}?tab=repositories"
    handle_pagination(_username, first_url)

    projectInfo['FORKED'] = forked

    _json = open(f"{_username}-projects.json",'w')
    _json.write(json.dumps(projectInfo))
    _json.close()

    

if __name__ == '__main__':
    username = input("Enter github username: ")
    scrape(username)
    print(f"Done! checkout your {username}-projects.json file at the root of this directory")


