ait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='CommentEditorweb__EditorBorder-sc-1tnt9hh-0 dXNXZI']"))
)
add.send_keys(comments)
add.send_keys(Keys.ENTER)