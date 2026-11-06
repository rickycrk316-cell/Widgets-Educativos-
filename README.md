# Widgets educativos · Quirúrgica 2 (PUCE, 10.º nivel)

Widgets HTML de estudio, autocontenidos y offline (skill `widget-ensenanza` v10, kit «Vademécum»). Abre el `.html` de cada tema en el navegador o en Archivos del iPad.

## Widgets

| Tema | Widget (HTML) | Modo | Entidades | `[VERIFICAR]` |
|---|---|---|---|---|
| Dolor abdominal | `Abdomen_agudo_quirurgico_widget_v10.html` | multi | apendicitis (principal), obstrucción, perforación, isquemia mesentérica, AAA roto (amenaza) | 42 |
| | `Dolor_biliopancreatico_widget_v10.html` | multi | colelitiasis/colecistitis (principal), coledocolitiasis, colangitis (amenaza), pancreatitis | 85 |
| | `Abdomen_agudo_medico_widget_v10.html` | multi | hipopotasemia con íleo (principal), saturnismo, porfiria aguda (amenaza) | 17 |
| Neoplasias GI | `Cancer_digestivo_alto_widget_v10.html` | multi | gástrico (principal y amenaza), cavidad oral, esófago, duodeno | 113 |
| | `Cancer_hepatobiliopancreatico_widget_v10.html` | multi | páncreas (principal y amenaza), hepatocelular, vesícula, colangiocarcinoma | 7 |
| | `Cancer_colorrectal_widget_v10.html` | mono | + pestaña de tamizaje y lesiones premalignas | 62 |
| Patología urinaria baja | `Patologia_urinaria_baja_widget_v10.html` | multi | HPB (principal), prostatitis, cáncer de próstata (amenaza), cistitis, uretritis · caso de Carlos | 38 |
| | `Prostatitis_cistitis_cancer_vesical_widget_v10.html` | multi | cistitis infecciosa (principal), prostatitis (amenaza), cáncer vesical | 15 |
| | `Cancer_de_prostata_widget_v10.html` | mono | cáncer de próstata | 7 |
| | `Definiciones_patologia_urinaria_baja.html` | definiciones | 9 términos + repaso | 0 |
| Disbasia infantil | `Cojera_dolorosa_sistemica_widget_v10.html` | multi | sinovitis transitoria (principal), artritis séptica (amenaza), osteomielitis, neoplasia ósea | 27 |
| | `Cojera_dolorosa_mecanica_widget_v10.html` | multi | Perthes (principal), epifisiólisis (amenaza), Osgood-Schlatter | 27 |
| | `Marcha_sin_dolor_widget_v10.html` | multi | DDC (principal), dismetría, neuromuscular, Guillain-Barré (amenaza) | 65 |
| | `Forma_piernas_pies_widget_v10.html` | multi | genu varo/valgo (principal), anteversión femoral, pie plano, pie cavo, equinovaro (amenaza) | 26 |
| Trastornos del ánimo | `Crisis_de_angustia_widget_v10.html` | multi | trastorno de pánico (principal), ansiedad generalizada, depresión mayor, consumo de benzodiacepinas, síndrome coronario agudo (amenaza) | 0 |
| | `Apertura_trastornos_animo.html` | apertura | caso + 9 términos, 12 problemas (B, P, S, FR), jerarquización, 4 hipótesis, repaso | 1 (composición de Stresstabs) |
| | `Depresion_bipolar_suicidio_widget_v10.html` | multi | depresión mayor (principal), trastorno bipolar, conducta suicida (amenaza) · esquema DSM-5-TR por entidad | 0 |

`[VERIFICAR]` = datos marcados `[VERIFICAR EN FUENTE]`: compruébalos antes de estudiar con ellos.

## Estructura

```
widgets/<tema>/PLAN.md          partición del caso en widgets y decisión del router
widgets/<tema>/*.html           widgets finales (generados: no editar a mano)
widgets/<tema>/<id>/            partes numeradas + manifiesto.json (aquí se edita)
kit/                            kit fijo, ensamblador y validadores
.claude/skills/impeccable/      revisión opcional (audit, polish, clarify)
fuentes/                        sílabos (dos rotaciones), kit v10 original, contratos de las skills, casos
docs/                           PRODUCT.md (propósito) y DESIGN.md (sistema visual)
```

## Reconstruir y validar

```sh
python3 kit/construir.py                          # todos
python3 kit/construir.py widgets/disbasia/sin_dolor
node kit/probar_navegador.js file://$PWD/widgets/<tema>/<widget>.html /tmp/capturas
```

Requiere `python3` con `beautifulsoup4` (se instala solo) y `node`. Las pruebas de navegador usan Playwright con el Chromium de `/opt/pw-browsers`.
