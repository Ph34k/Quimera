**PDFs**: Instruções rápidas

- **Purpose**: Copy chapter/guide PDF files from a source folder into the project so they can be served or packaged.
- **Script**: `scripts/import_pdfs.py` — procura por nomes de arquivo esperados e copia para `docs/pdfs`.
- **Quick usage**:

```
python scripts/import_pdfs.py --source-dir "C:/Users/henri_6m1hz7q/OneDrive/Documentos/quimera"
```

- **If some PDFs are missing**: o script lista os arquivos não encontrados. Copie manualmente os PDFs para `projeto-quimera/docs/pdfs` ou ajuste os nomes esperados em `EXPECTED_PDFS` no script.

**Notas**:
- O script não altera ou modifica os PDFs; apenas copia os arquivos encontrados.
- Você pode ajustar a lista `EXPECTED_PDFS` para corresponder aos nomes reais dos seus PDFs.