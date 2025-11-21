# دليل إعداد مشروع Odoo Zebra Label

## 1. إنشاء الهيكل الأساسي للمشروع

``` bash
mkdir -p ~/مستقل/odoo_zebra_label/odoo-test/addons/odoo_zebra_label
cd ~/مستقل/odoo_zebra_label
```

## 2. إنشاء ملف Docker Compose

``` bash
cat > odoo-test/docker-compose.yml << 'EOF'
version: '3.1'
services:
  web:
    image: odoo:16.0
    container_name: odoo-zebra-test
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./addons:/mnt/extra-addons
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
    restart: unless-stopped

  db:
    image: postgres:13
    container_name: postgres-zebra-db
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
    restart: unless-stopped

volumes:
  odoo-web-data:
  odoo-db-data:
EOF
```

## 3. إنشاء ملفات الموديول الأساسية

### ملف `__manifest__.py`

``` bash
cat > odoo-test/addons/odoo_zebra_label/__manifest__.py << 'EOF'
{
    'name': 'Zebra Label Printer',
    'version': '1.0',
    'summary': 'Professional Labels for Zebra ZD220',
    'depends': ['base', 'product', 'stock'],
    'category': 'Inventory',
    'data': [
        'data/paperformat.xml',
        'report/label_template.xml',
        'report/label_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
EOF
```

### ملف paperformat.xml

``` bash
mkdir -p odoo-test/addons/odoo_zebra_label/data
cat > odoo-test/addons/odoo_zebra_label/data/paperformat.xml << 'EOF'
<odoo>
    <data noupdate="1">
        <record id="paperformat_zebra_pro" model="report.paperformat">
            <field name="name">Zebra ZD220 Pro Label (60x40mm)</field>
            <field name="default" eval="True"/>
            <field name="format">custom</field>
            <field name="page_width">60</field>
            <field name="page_height">40</field>
            <field name="orientation">Portrait</field>
            <field name="margin_top">0</field>
            <field name="margin_bottom">0</field>
            <field name="margin_left">0</field>
            <field name="margin_right">0</field>
            <field name="dpi">300</field>
            <field name="header_line" eval="False"/>
            <field name="header_spacing">0</field>
            <field name="line_page" eval="False"/>
        </record>
    </data>
</odoo>
EOF
```

### قالب الملصق label_template.xml

``` bash
mkdir -p odoo-test/addons/odoo_zebra_label/report
cat > odoo-test/addons/odoo_zebra_label/report/label_template.xml << 'EOF'
<odoo>
    <template id="zebra_label_template">
        <t t-call="web.html_container">
            <t t-call="web.external_layout">
                <style>
                    .professional-label {
                        width: 60mm;
                        height: 40mm;
                        padding: 1mm;
                        font-family: 'Arial', sans-serif;
                        text-align: center;
                        border: 0.2mm solid #e0e0e0;
                        box-sizing: border-box;
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        background: white;
                    }
                    .product-name {
                        font-size: 8px;
                        font-weight: bold;
                        color: #2c3e50;
                        margin: 0.5mm 0;
                    }
                    .product-details {
                        font-size: 6px;
                        color: #5a6c7d;
                        margin: 0.3mm 0;
                    }
                    .price-tag {
                        background: #27ae60;
                        color: white;
                        padding: 0.5mm;
                        border-radius: 1mm;
                        font-size: 7px;
                        font-weight: bold;
                    }
                </style>

                <t t-foreach="docs" t-as="product">
                    <div class="professional-label">
                        <div class="product-name">
                            <t t-esc="product.name or 'PRODUCT'"/>
                        </div>

                        <div class="product-details">
                            <div t-if="product.default_code">
                                <strong>REF:</strong> <t t-esc="product.default_code"/>
                            </div>
                            <div t-if="product.barcode">
                                <strong>BARCODE:</strong> <t t-esc="product.barcode"/>
                            </div>
                        </div>

                        <div class="price-tag">
                            <t t-if="product.lst_price">
                                <t t-esc="'%.2f' % product.lst_price"/> DZD
                            </t>
                            <t t-else>
                                PRICE: N/A
                            </t>
                        </div>
                    </div>
                </t>
            </t>
        </t>
    </template>
</odoo>
EOF
```

### تقرير الطباعة label_report.xml

``` bash
cat > odoo-test/addons/odoo_zebra_label/report/label_report.xml << 'EOF'
<odoo>
    <data>
        <report
            id="action_zebra_label"
            string="Zebra Professional Label"
            model="product.product"
            report_type="qweb-pdf"
            name="odoo_zebra_label.zebra_label_template"
            paperformat="odoo_zebra_label.paperformat_zebra_pro"
        />
    </data>
</odoo>
EOF
```

------------------------------------------------------------------------

## الجزء الثاني: التشغيل والتجربة

### تشغيل الحاويات

``` bash
cd ~/مستقل/odoo_zebra_label/odoo-test
docker-compose up -d
```

### مراقبة السجلات

``` bash
docker-compose logs -f web
```

### الوصول للتطبيق

افتح المتصفح واذهب إلى:\
http://localhost:8069

------------------------------------------------------------------------

## الجزء الثالث: إعداد Odoo

### إنشاء قاعدة البيانات

-   Database Name: **zebra_production**
-   Email: بريدك الإلكتروني\
-   Password: كلمة سر قوية

### تثبيت التطبيقات

Install: - Sales\
- Inventory

### تفعيل وضع المطور

Settings → Developer Mode → Activate

### تثبيت الموديول

Apps → Update Apps List → ابحث عن **Zebra** → Install

------------------------------------------------------------------------

## اختبار النظام

### 1. إنشاء منتج:

    Product Name: iPhone 15 Pro Test
    Product Type: Storable Product
    Sales Price: 2500.00
    Internal Reference: IPH15-TEST
    Barcode: 1234567890123

### 2. طباعة الملصق

Product → Print → Zebra Professional Label

------------------------------------------------------------------------

## استكشاف الأخطاء

``` bash
docker-compose logs web | grep -i error
docker-compose down
docker-compose up -d --force-recreate
```

------------------------------------------------------------------------

🎉 **مبروك! النظام جاهز بالكامل.**
