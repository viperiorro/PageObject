def test_all_categories_are_present(logged_in_catalog_page):
    logged_in_catalog_page.verify_categories_in_sidebar_present()
    logged_in_catalog_page.verify_categories_in_quick_links_present()
    logged_in_catalog_page.verify_categories_in_main_image_content_present()