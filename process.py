from link_checker import LinkChecker


link_checker = LinkChecker()
link_checker.start()


print('\nProcessed in %s minutes\n' % link_checker.get_elapsed_minutes())