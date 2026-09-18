
Herramienta en Python que extrae datos estructurados de facturas en PDF —formato español e internacional— y exporta el resultado a Excel. Proyecto de portfolio pensado para demostrar extracción de datos basada en reglas, con una estructura de proyecto cuidada y probada contra un conjunto de datos variado.

Qué hace
Lee el contenido de texto de una factura en PDF (pdfplumber).
Detecta el formato (español vs. internacional) puntuando marcadores propios del dominio que aparecen en el texto (IVA, NIF, € frente a VAT, Tax ID, $, etc.) — no mediante detección de idioma, ya que el objetivo es identificar qué conjunto de reglas fiscales/de formato aplicar, no el idioma en sí.
Extrae los campos clave con expresiones regulares específicas para cada formato:
Número de factura
Fecha de emisión
Emisor / proveedor
Importe total
Escribe cada factura procesada como una nueva fila en un archivo Excel (openpyxl), creando el archivo con cabeceras en la primera ejecución y añadiendo filas en las siguientes.

El pipeline procesa, en una sola ejecución, todos los PDF que encuentre en data/input/.

Estructura del proyecto
invoice-extractor/
├── data/
│   ├── input/          # aquí van las facturas en PDF
│   └── output/         # Excel generado (ignorado por git)
├── src/
│   ├── config.py         # rutas base (relativas a la raíz del proyecto, independientes del SO)
│   ├── extractor.py       # PDF → texto plano
│   ├── parser.py          # detección de formato + extracción de campos (regex)
│   ├── excel_writer.py    # datos estructurados → fila de Excel
│   └── main.py            # orquesta el pipeline completo
├── .env.example            # plantilla para el futuro uso de la API de OpenAI
├── requirements.txt
└── README.es.md
Instalación
bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell

# source .venv/bin/activate       # macOS/Linux

pip install -r requirements.txt
Uso
Coloca una o varias facturas en PDF dentro de data/input/.
Ejecuta el pipeline desde la raíz del proyecto:
bash
python src/main.py
Revisa data/output/Facture_results.xlsx para ver los resultados extraídos.
Limitaciones conocidas
La extracción del emisor depende de que la factura use una forma jurídica reconocible (S.L., S.A., Ltd., Inc., LLC). Empresas con otras siglas (p. ej. S.L.U., GmbH) no se capturarían correctamente.
La extracción de campos es basada en regex y determinista — fiable y auditable para los formatos contra los que se ha construido, pero no generaliza a diseños de factura que no ha visto antes. Es una decisión deliberada para datos financieros: que un campo salga vacío (None) es más seguro que uno incorrecto de forma silenciosa generado por un modelo probabilístico.
Probado contra un conjunto sintético de ~60 facturas en dos formatos y ~25 países; no validado contra facturas reales escaneadas.
Próximos pasos
Paso de validación: marcar para revisión manual las facturas con campos ausentes, en vez de escribir filas incompletas sin avisar.
Categorización de conceptos con LLM: clasificar los conceptos de la factura (materiales, servicios, etc.) con un LLM — una tarea de interpretación, no de extracción exacta, donde el riesgo de un LLM es asumible.
LLM como respaldo, no como opción por defecto: cuando la extracción por regex falle, intentar la extracción vía LLM como último recurso, marcada claramente como de menor confianza.
Extracción por coordenadas: resolver los diseños de PDF a dos columnas (emisor/cliente lado a lado) usando la posición de las palabras en la página, en vez de la heurística actual basada en la forma jurídica.
