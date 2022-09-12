from PyQt5.QtWidgets import QVBoxLayout, QDialog, QTextEdit


class ResultDialog(QDialog):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_dict = {}
        self.data = data
        # print(self.data)

        self.init_ui()

    def init_ui(self):
        """
        初始化对话框
        :return:
        """
        self.setWindowTitle("result")
        self.resize(200, 200)
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setText("")

        layout.addWidget(text_edit)
        self.setLayout(layout)

        text_edit.setText(self.data)
