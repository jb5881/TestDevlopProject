from page.base_page import BasePage


class ImportContact(BasePage):
    def upload_file(self, name: list, *args):
        self._params['value'] = args
        text = self.steps('../page/import_contact.yml', name)
        return text
