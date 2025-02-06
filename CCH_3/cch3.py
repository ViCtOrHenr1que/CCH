from abc import ABC, abstractmethod

class ProcessadorDeDocumento(ABC):
    def processar_documento(self):
        self.abrir_documento()
        self.analisar_conteudo()
        self.salvar_documento()

    @abstractmethod
    def abrir_documento(self):
        pass

    @abstractmethod
    def analisar_conteudo(self):
        pass

    @abstractmethod
    def salvar_documento(self):
        pass

class ProcessadorPDF(ProcessadorDeDocumento):
    def abrir_documento(self):
        print("Abrindo documento PDF...")

    def analisar_conteudo(self):
        print("Analisando conteúdo do PDF...")

    def salvar_documento(self):
        print("Salvando documento PDF.")

class ProcessadorWord(ProcessadorDeDocumento):
    def abrir_documento(self):
        print("Abrindo documento Word...")

    def analisar_conteudo(self):
        print("Analisando conteúdo do Word...")

    def salvar_documento(self):
        print("Salvando documento Word.")

documentos = [ProcessadorPDF(), ProcessadorWord()]
for documento in documentos:
    documento.processar_documento()
    print("-------------------------")