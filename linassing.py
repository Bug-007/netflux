
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_linkedin_job_posting(url):
    driver = webdriver.Firefox()
    driver.get(url)

    # Get the job poster's name
    str = ".base-main-card__info:nth-child(2) > .base-main-card__title"
    job_poster_name = driver.find_element(By.CSS_SELECTOR, str).text
    print("Job Poster's Name : "+job_poster_name)
    # str = ".message-the-recruiter"
    job_poster_name = driver.find_element(By.CSS_SELECTOR, str)
    # element = driver.find_element(By.CSS_SELECTOR, str)
    # elements = element.find_elements(By.TAG_NAME, 'p')
    # for e in elements:
    #     print(e.text)
    # Get the "About the Job" section

    # clicking to show more

    show_more = driver.find_element(By.CSS_SELECTOR, ".show-more-less-html__button--more")
    show_more.click()

    jd_disc = driver.find_element(By.CSS_SELECTOR, ".details")
    jd_discs = jd_disc.find_elements(By.TAG_NAME, 'p')
    print("\n\nAbout the job")
    for e in jd_discs:
        print(e.text)


if __name__ == "__main__":
    url = "https://www.linkedin.com/jobs/view/3660532900"
    scrape_linkedin_job_posting(url)

