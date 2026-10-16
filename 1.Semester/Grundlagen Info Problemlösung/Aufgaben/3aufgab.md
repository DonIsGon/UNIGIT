---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
#include <stdio.h>

int main()
{
int n;
printf("Geben Sie eine positive ganze Zahl ein: "); //fehlende Klammer
scanf("%d", &n);
printf("Die Fakultaet von %d ist: ", n);
int f = 1; //fehlende Deklarierung von f
while (n > 0) //noch eine fehlende Klammer
{
f = f * n; //Tippfehler statt n wurde m geschrieben
n = n - 1;
}
printf("%d\n", f);
return 0; //fehlendes ;
} ^kdzzmjpj

#include <stdio.h> //muss auch noch eingefügt werden damit scanf funktioniert

int main()
{
int n, i, q;
printf("Geben Sie eine positive ganze Zahl ein: "); //Vergessenes "
scanf("%d", &n);
q = 0; // es muss erst die variable stehen nicht 0 = q
for (i = n; i > 0; i = i / 10)
q = q + (i % 10); // fehlendes ;
printf("Die Quersumme von %d ist: %d\n", n, q); // nach n fehlt ein ,
return 0;
}
 ^kJhVRLya

## Embedded Files
ace05a52f542a505c0415daf3439cc7a33230cd2: [[aufgabenblatt03.pdf#page=1]]

a180b908dfe535c9facf6b6f0a7aa2a399b08987: [[aufgabenblatt03.pdf#page=2]]

%%
## Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.16.1",
	"elements": [
		{
			"id": "2wxARIRo",
			"type": "rectangle",
			"x": -833.5,
			"y": -2362,
			"width": 1667,
			"height": 2357,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 87483,
			"version": 5,
			"versionNonce": 597224501,
			"updated": 1762280117402,
			"isDeleted": false,
			"groupIds": [
				"wAR03nZv",
				"wt4Rnrgp"
			],
			"boundElements": [],
			"link": null,
			"locked": true,
			"frameId": null,
			"index": "Zz"
		},
		{
			"id": "ncVfk7jR",
			"type": "image",
			"x": -833.5,
			"y": -2362,
			"width": 1667,
			"height": 2357,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 96539,
			"version": 2,
			"versionNonce": 1756529314,
			"updated": 1762258476316,
			"isDeleted": false,
			"groupIds": [
				"wAR03nZv",
				"wt4Rnrgp"
			],
			"boundElements": [],
			"link": null,
			"locked": true,
			"frameId": null,
			"fileId": "ace05a52f542a505c0415daf3439cc7a33230cd2",
			"scale": [
				1,
				1
			],
			"crop": null,
			"index": "a1",
			"status": "pending",
			"customData": {
				"pdfPageViewProps": {
					"left": 0,
					"bottom": 0,
					"right": 595.276,
					"top": 841.89,
					"rotate": 0
				}
			}
		},
		{
			"id": "7JWPrOep",
			"type": "rectangle",
			"x": -833.5,
			"y": 5,
			"width": 1667,
			"height": 2357,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 53137,
			"version": 2,
			"versionNonce": 329642110,
			"updated": 1762258476316,
			"isDeleted": false,
			"groupIds": [
				"CrHQHZym",
				"wt4Rnrgp"
			],
			"boundElements": [],
			"link": null,
			"locked": true,
			"frameId": null,
			"index": "a2"
		},
		{
			"id": "61pKWBxg",
			"type": "image",
			"x": -833.5,
			"y": 5,
			"width": 1667,
			"height": 2357,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 8669,
			"version": 2,
			"versionNonce": 1447943778,
			"updated": 1762258476316,
			"isDeleted": false,
			"groupIds": [
				"CrHQHZym",
				"wt4Rnrgp"
			],
			"boundElements": [],
			"link": null,
			"locked": true,
			"frameId": null,
			"fileId": "a180b908dfe535c9facf6b6f0a7aa2a399b08987",
			"scale": [
				1,
				1
			],
			"crop": null,
			"index": "a3",
			"status": "pending",
			"customData": {
				"pdfPageViewProps": {
					"left": 0,
					"bottom": 0,
					"right": 595.276,
					"top": 841.89,
					"rotate": 0
				}
			}
		},
		{
			"id": "kdzzmjpj",
			"type": "text",
			"x": -807.2884947449561,
			"y": 2540.2217279083147,
			"width": 621.71923828125,
			"height": 425,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"index": "a6",
			"roundness": null,
			"seed": 2080944795,
			"version": 28,
			"versionNonce": 579075579,
			"isDeleted": false,
			"boundElements": [],
			"updated": 1762266421325,
			"link": null,
			"locked": false,
			"text": "#include <stdio.h>\n\nint main()\n{\nint n;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //fehlende Klammer\nscanf(\"%d\", &n);\nprintf(\"Die Fakultaet von %d ist: \", n);\nint f = 1; //fehlende Deklarierung von f\nwhile (n > 0) //noch eine fehlende Klammer\n{\nf = f * n; //Tippfehler statt n wurde m geschrieben\nn = n - 1;\n}\nprintf(\"%d\\n\", f);\nreturn 0; //fehlendes ;\n}",
			"rawText": "#include <stdio.h>\n\nint main()\n{\nint n;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //fehlende Klammer\nscanf(\"%d\", &n);\nprintf(\"Die Fakultaet von %d ist: \", n);\nint f = 1; //fehlende Deklarierung von f\nwhile (n > 0) //noch eine fehlende Klammer\n{\nf = f * n; //Tippfehler statt n wurde m geschrieben\nn = n - 1;\n}\nprintf(\"%d\\n\", f);\nreturn 0; //fehlendes ;\n}",
			"fontSize": 20,
			"fontFamily": 6,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "#include <stdio.h>\n\nint main()\n{\nint n;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //fehlende Klammer\nscanf(\"%d\", &n);\nprintf(\"Die Fakultaet von %d ist: \", n);\nint f = 1; //fehlende Deklarierung von f\nwhile (n > 0) //noch eine fehlende Klammer\n{\nf = f * n; //Tippfehler statt n wurde m geschrieben\nn = n - 1;\n}\nprintf(\"%d\\n\", f);\nreturn 0; //fehlendes ;\n}",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"id": "kJhVRLya",
			"type": "text",
			"x": -806.1319645473627,
			"y": 3075.0738830478194,
			"width": 710.2990112304688,
			"height": 350,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"index": "a7",
			"roundness": null,
			"seed": 1382520411,
			"version": 151,
			"versionNonce": 2080722043,
			"isDeleted": false,
			"boundElements": [],
			"updated": 1762267202931,
			"link": null,
			"locked": false,
			"text": "#include <stdio.h> //muss auch noch eingefügt werden damit scanf funktioniert\n\nint main()\n{\nint n, i, q;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //Vergessenes \"\nscanf(\"%d\", &n);\nq = 0; // es muss erst die variable stehen nicht 0 = q\nfor (i = n; i > 0; i = i / 10)\nq = q + (i % 10); // fehlendes ;\nprintf(\"Die Quersumme von %d ist: %d\\n\", n, q); // nach n fehlt ein ,\nreturn 0;\n}\n",
			"rawText": "#include <stdio.h> //muss auch noch eingefügt werden damit scanf funktioniert\n\nint main()\n{\nint n, i, q;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //Vergessenes \"\nscanf(\"%d\", &n);\nq = 0; // es muss erst die variable stehen nicht 0 = q\nfor (i = n; i > 0; i = i / 10)\nq = q + (i % 10); // fehlendes ;\nprintf(\"Die Quersumme von %d ist: %d\\n\", n, q); // nach n fehlt ein ,\nreturn 0;\n}\n",
			"fontSize": 20,
			"fontFamily": 6,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "#include <stdio.h> //muss auch noch eingefügt werden damit scanf funktioniert\n\nint main()\n{\nint n, i, q;\nprintf(\"Geben Sie eine positive ganze Zahl ein: \"); //Vergessenes \"\nscanf(\"%d\", &n);\nq = 0; // es muss erst die variable stehen nicht 0 = q\nfor (i = n; i > 0; i = i / 10)\nq = q + (i % 10); // fehlendes ;\nprintf(\"Die Quersumme von %d ist: %d\\n\", n, q); // nach n fehlt ein ,\nreturn 0;\n}\n",
			"autoResize": true,
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 6,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"currentItemArrowType": "round",
		"currentItemFrameRole": null,
		"scrollX": 3996.7558325600426,
		"scrollY": 2214.7199815586346,
		"zoom": {
			"value": 0.136861
		},
		"currentItemRoundness": "round",
		"gridSize": 20,
		"gridStep": 5,
		"gridModeEnabled": false,
		"gridColor": {
			"Bold": "rgba(217, 217, 217, 0.5)",
			"Regular": "rgba(230, 230, 230, 0.5)"
		},
		"currentStrokeOptions": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true,
			"markerName": true,
			"markerEnabled": true
		},
		"objectsSnapModeEnabled": false,
		"activeTool": {
			"type": "selection",
			"customType": null,
			"locked": false,
			"fromSelection": false,
			"lastActiveTool": null
		}
	},
	"files": {}
}
```
%%