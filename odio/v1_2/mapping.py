from types import MappingProxyType

EM = {
    "office:document-content": {
        "allowed_attributes": {
            "grddl:transformation",
            "office:version",
            "xmlns:anim",
            "xmlns:chart",
            "xmlns:config",
            "xmlns:db",
            "xmlns:dr3d",
            "xmlns:draw",
            "xmlns:form",
            "xmlns:meta",
            "xmlns:number",
            "xmlns:office",
            "xmlns:presentation",
            "xmlns:script",
            "xmlns:table",
            "xmlns:text",
            "xmlns:style",
            "xmlns:fo",
            "xmlns:svg",
            "xmlns:smil",
            "xmlns:dc",
            "xmlns:math",
            "xmlns:xforms",
            "xmlns:xlink",
            "xmlns:xhtml",
            "xmlns:grddl",
            "xmlns:of",
        },
        "allowed_children": {
            "office:automatic-styles",
            "office:body",
            "office:font-face-decls",
            "office:scripts",
        },
    },
    "office:document-meta": {
        "allowed_attributes": {
            "grddl:transformation",
            "office:version",
            "xmlns:office",
            "xmlns:xlink",
            "xmlns:dc",
            "xmlns:meta",
            "xmlns:of",
        },
        "allowed_children": {"office:meta"},
    },
    "office:document-settings": {
        "allowed_attributes": {
            "grddl:transformation",
            "office:version",
            "xmlns:office",
            "xmlns:xlink",
            "xmlns:config",
            "xmlns:of",
        },
        "allowed_children": {"office:settings"},
    },
    "office:document-styles": {
        "allowed_attributes": {
            "grddl:transformation",
            "office:version",
            "xmlns:anim",
            "xmlns:chart",
            "xmlns:config",
            "xmlns:db",
            "xmlns:dr3d",
            "xmlns:draw",
            "xmlns:form",
            "xmlns:meta",
            "xmlns:number",
            "xmlns:office",
            "xmlns:presentation",
            "xmlns:script",
            "xmlns:table",
            "xmlns:text",
            "xmlns:style",
            "xmlns:odf",
            "xmlns:fo",
            "xmlns:svg",
            "xmlns:smil",
            "xmlns:dc",
            "xmlns:math",
            "xmlns:xforms",
            "xmlns:xlink",
            "xmlns:xhtml",
            "xmlns:grddl",
            "xmlns:pkg",
            "xmlns:of",
        },
        "allowed_children": {
            "office:automatic-styles",
            "office:font-face-decls",
            "office:master-styles",
            "office:styles",
        },
    },
    "office:spreadsheet": {
        "allowed_attributes": {
            "table:protection-key",
            "table:protection-key-digest-algorithm",
            "table:structure-protected",
        },
        "allowed_children": {
            "table:calculation-settings",
            "table:consolidation",
            "table:content-validations",
            "table:database-ranges",
            "table:data-pilot-tables",
            "table:dde-links",
            "table:label-ranges",
            "table:named-expressions",
            "table:table",
            "table:tracked-changes",
            "text:alphabetical-index-auto-mark-file",
            "text:dde-connection-decls",
            "text:sequence-decls",
            "text:user-field-decls",
            "text:variable-decls",
        },
    },
    "office:text": {
        "allowed_attributes": {"text:global", "text:use-soft-page-breaks"},
        "allowed_children": {
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:forms",
            "table:calculation-settings",
            "table:consolidation",
            "table:content-validations",
            "table:database-ranges",
            "table:data-pilot-tables",
            "table:dde-links",
            "table:label-ranges",
            "table:named-expressions",
            "table:table",
            "text:alphabetical-index",
            "text:alphabetical-index-auto-mark-file",
            "text:bibliography",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:dde-connection-decls",
            "text:h",
            "text:illustration-index",
            "text:list",
            "text:numbered-paragraph",
            "text:object-index",
            "text:p",
            "text:page-sequence",
            "text:section",
            "text:sequence-decls",
            "text:soft-page-break",
            "text:table-index",
            "text:table-of-content",
            "text:tracked-changes",
            "text:user-field-decls",
            "text:user-index",
            "text:variable-decls",
        },
    },
    "manifest:file-entry": {
        "allowed_attributes": {
            "manifest:full-path",
            "manifest:media-type",
            "manifest:preferred-view-mode",
            "manifest:size",
            "manifest:version",
        },
        "allowed_children": {"manifest:encryption-data"},
    },
    "manifest:manifest": {
        "allowed_attributes": {"manifest:version", "xmlns:manifest"},
        "allowed_children": {"manifest:file-entry"},
    },
    "number:date-style": {
        "allowed_attributes": {
            "number:automatic-order",
            "number:country",
            "number:format-source",
            "number:language",
            "number:rfc-language-tag",
            "number:script",
            "number:title",
            "number:transliteration-country",
            "number:transliteration-format",
            "number:transliteration-language",
            "number:transliteration-style",
            "style:display-name",
            "style:name",
            "style:volatile",
        },
        "allowed_children": {
            "number:am-pm",
            "number:day",
            "number:day-of-week",
            "number:era",
            "number:hours",
            "number:minutes",
            "number:month",
            "number:quarter",
            "number:seconds",
            "number:text",
            "number:week-of-year",
            "number:year",
            "style:map",
            "style:text-properties",
        },
    },
    "number:year": {
        "allowed_attributes": {"number:calendar", "number:style"},
        "allowed_children": {},
    },
    "number:text": {
        "allowed_attributes": {},
        "allowed_children": {str},
    },
    "number:month": {
        "allowed_attributes": {
            "number:calendar",
            "number:possessive-form",
            "number:style",
            "number:textual",
        },
        "allowed_children": {},
    },
    "number:day": {
        "allowed_attributes": {
            "number:calendar",
            "number:style",
        },
        "allowed_children": {},
    },
    "number:hours": {
        "allowed_attributes": {
            "number:style",
        },
        "allowed_children": {},
    },
    "number:minutes": {
        "allowed_attributes": {
            "number:style",
        },
        "allowed_children": {},
    },
    "table:table": {
        "allowed_attributes": {
            "table:is-sub-table",
            "table:name",
            "table:print",
            "table:print-ranges",
            "table:protected",
            "table:protection-key",
            "table:protection-key-digest-algorithm",
            "table:style-name",
            "table:template-name",
            "table:use-banding-columns-styles",
            "table:use-banding-rows-styles",
            "table:use-first-column-styles",
            "table:use-first-row-styles",
            "table:use-last-column-styles",
            "table:use-last-row-styles",
            "xml:id",
        },
        "allowed_children": {
            "office:dde-source",
            "office:forms",
            "table:desc",
            "table:named-expressions",
            "table:scenario",
            "table:shapes",
            "table:table-column",
            "table:table-column-group",
            "table:table-columns",
            "table:table-header-columns",
            "table:table-header-rows",
            "table:table-row",
            "table:table-row-group",
            "table:table-rows",
            "table:table-source",
            "table:title",
            "text:soft-page-break",
        },
    },
    "table:table-row": {
        "allowed_attributes": {
            "table:default-cell-style-name",
            "table:number-rows-repeated",
            "table:style-name",
            "table:visibility",
            "xml:id",
        },
        "allowed_children": {"table:covered-table-cell", "table:table-cell"},
    },
    "text:a": {
        "allowed_attributes": {
            "office:name",
            "office:target-frame-name",
            "office:title",
            "text:style-name",
            "text:visited-style-name",
            "xlink:actuate",
            "xlink:href",
            "xlink:show",
            "xlink:type",
        },
        "allowed_children": {
            str,
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:annotation",
            "office:annotation-end",
            "office:event-listeners",
            "presentation:date-time",
            "presentation:footer",
            "presentation:header",
            "text:alphabetical-index-mark",
            "text:alphabetical-index-mark-end",
            "text:alphabetical-index-mark-start",
            "text:author-initials",
            "text:author-name",
            "text:bibliography-mark",
            "text:bookmark",
            "text:bookmark-end",
            "text:bookmark-ref",
            "text:bookmark-start",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:chapter",
            "text:character-count",
            "text:conditional-text",
            "text:creation-date",
            "text:creation-time",
            "text:creator",
            "text:database-display",
            "text:database-name",
            "text:database-next",
            "text:database-row-number",
            "text:database-row-select",
            "text:date",
            "text:dde-connection",
            "text:description",
            "text:editing-cycles",
            "text:editing-duration",
            "text:execute-macro",
            "text:expression",
            "text:file-name",
            "text:hidden-paragraph",
            "text:hidden-text",
            "text:image-count",
            "text:initial-creator",
            "text:keywords",
            "text:line-break",
            "text:measure",
            "text:meta",
            "text:meta-field",
            "text:modification-date",
            "text:modification-time",
            "text:note",
            "text:note-ref",
            "text:object-count",
            "text:page-continuation",
            "text:page-count",
            "text:page-number",
            "text:page-variable-get",
            "text:page-variable-set",
            "text:paragraph-count",
            "text:placeholder",
            "text:print-date",
            "text:printed-by",
            "text:print-time",
            "text:reference-mark",
            "text:reference-mark-end",
            "text:reference-mark-start",
            "text:reference-ref",
            "text:ruby",
            "text:s",
            "text:script",
            "text:sender-city",
            "text:sender-company",
            "text:sender-country",
            "text:sender-email",
            "text:sender-fax",
            "text:sender-firstname",
            "text:sender-initials",
            "text:sender-lastname",
            "text:sender-phone-private",
            "text:sender-phone-work",
            "text:sender-position",
            "text:sender-postal-code",
            "text:sender-state-or-province",
            "text:sender-street",
            "text:sender-title",
            "text:sequence",
            "text:sequence-ref",
            "text:sheet-name",
            "text:soft-page-break",
            "text:span",
            "text:subject",
            "text:tab",
            "text:table-count",
            "text:table-formula",
            "text:template-name",
            "text:text-input",
            "text:time",
            "text:title",
            "text:toc-mark",
            "text:toc-mark-end",
            "text:toc-mark-start",
            "text:user-defined",
            "text:user-field-get",
            "text:user-field-input",
            "text:user-index-mark",
            "text:user-index-mark-end",
            "text:user-index-mark-start",
            "text:variable-get",
            "text:variable-input",
            "text:variable-set",
            "text:word-count",
        },
    },
    "table:table-cell": {
        "allowed_attributes": {
            "office:boolean-value",
            "office:currency",
            "office:date-value",
            "office:string-value",
            "office:time-value",
            "office:value",
            "office:value-type",
            "table:content-validation-name",
            "table:formula",
            "table:number-columns-repeated",
            "table:number-columns-spanned",
            "table:number-matrix-columns-spanned",
            "table:number-matrix-rows-spanned",
            "table:number-rows-spanned",
            "table:protect",
            "table:protected",
            "table:style-name",
            "xhtml:about",
            "xhtml:content",
            "xhtml:datatype",
            "xhtml:property",
            "xml:id",
        },
        "allowed_children": {
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:annotation",
            "table:cell-range-source",
            "table:detective",
            "table:table",
            "text:alphabetical-index",
            "text:bibliography",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:h",
            "text:illustration-index",
            "text:list",
            "text:numbered-paragraph",
            "text:object-index",
            "text:p",
            "text:section",
            "text:soft-page-break",
            "text:table-index",
            "text:table-of-content",
            "text:user-index",
        },
    },
    "text:h": {
        "allowed_attributes": {
            "text:class-names",
            "text:cond-style-name",
            "text:id",
            "text:is-list-header",
            "text:outline-level",
            "text:restart-numbering",
            "text:start-value",
            "text:style-name",
            "xhtml:about",
            "xhtml:content",
            "xhtml:datatype",
            "xhtml:property",
            "xml:id",
        },
        "allowed_children": {
            str,
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:annotation",
            "office:annotation-end",
            "presentation:date-time",
            "presentation:footer",
            "presentation:header",
            "text:a",
            "text:alphabetical-index-mark",
            "text:alphabetical-index-mark-end",
            "text:alphabetical-index-mark-start",
            "text:author-initials",
            "text:author-name",
            "text:bibliography-mark",
            "text:bookmark",
            "text:bookmark-end",
            "text:bookmark-ref",
            "text:bookmark-start",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:chapter",
            "text:character-count",
            "text:conditional-text",
            "text:creation-date",
            "text:creation-time",
            "text:creator",
            "text:database-display",
            "text:database-name",
            "text:database-next",
            "text:database-row-number",
            "text:database-row-select",
            "text:date",
            "text:dde-connection",
            "text:description",
            "text:editing-cycles",
            "text:editing-duration",
            "text:execute-macro",
            "text:expression",
            "text:file-name",
            "text:hidden-paragraph",
            "text:hidden-text",
            "text:image-count",
            "text:initial-creator",
            "text:keywords",
            "text:line-break",
            "text:measure",
            "text:meta",
            "text:meta-field",
            "text:modification-date",
            "text:modification-time",
            "text:note",
            "text:note-ref",
            "text:number",
            "text:object-count",
            "text:page-continuation",
            "text:page-count",
            "text:page-number",
            "text:page-variable-get",
            "text:page-variable-set",
            "text:paragraph-count",
            "text:placeholder",
            "text:print-date",
            "text:printed-by",
            "text:print-time",
            "text:reference-mark",
            "text:reference-mark-end",
            "text:reference-mark-start",
            "text:reference-ref",
            "text:ruby",
            "text:s",
            "text:script",
            "text:sender-city",
            "text:sender-company",
            "text:sender-country",
            "text:sender-email",
            "text:sender-fax",
            "text:sender-firstname",
            "text:sender-initials",
            "text:sender-lastname",
            "text:sender-phone-private",
            "text:sender-phone-work",
            "text:sender-position",
            "text:sender-postal-code",
            "text:sender-state-or-province",
            "text:sender-street",
            "text:sender-title",
            "text:sequence",
            "text:sequence-ref",
            "text:sheet-name",
            "text:soft-page-break",
            "text:span",
            "text:subject",
            "text:tab",
            "text:table-count",
            "text:table-formula",
            "text:template-name",
            "text:text-input",
            "text:time",
            "text:title",
            "text:toc-mark",
            "text:toc-mark-end",
            "text:toc-mark-start",
            "text:user-defined",
            "text:user-field-get",
            "text:user-field-input",
            "text:user-index-mark",
            "text:user-index-mark-end",
            "text:user-index-mark-start",
            "text:variable-get",
            "text:variable-input",
            "text:variable-set",
            "text:word-count",
        },
    },
    "text:p": {
        "allowed_attributes": {
            "text:class-names",
            "text:cond-style-name",
            "text:id",
            "text:style-name",
            "xhtml:about",
            "xhtml:content",
            "xhtml:datatype",
            "xhtml:property",
            "xml:id",
        },
        "allowed_children": {
            str,
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:annotation",
            "office:annotation-end",
            "presentation:date-time",
            "presentation:footer",
            "presentation:header",
            "text:a",
            "text:alphabetical-index-mark",
            "text:alphabetical-index-mark-end",
            "text:alphabetical-index-mark-start",
            "text:author-initials",
            "text:author-name",
            "text:bibliography-mark",
            "text:bookmark",
            "text:bookmark-end",
            "text:bookmark-ref",
            "text:bookmark-start",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:chapter",
            "text:character-count",
            "text:conditional-text",
            "text:creation-date",
            "text:creation-time",
            "text:creator",
            "text:database-display",
            "text:database-name",
            "text:database-next",
            "text:database-row-number",
            "text:database-row-select",
            "text:date",
            "text:dde-connection",
            "text:description",
            "text:editing-cycles",
            "text:editing-duration",
            "text:execute-macro",
            "text:expression",
            "text:file-name",
            "text:hidden-paragraph",
            "text:hidden-text",
            "text:image-count",
            "text:initial-creator",
            "text:keywords",
            "text:line-break",
            "text:measure",
            "text:meta",
            "text:meta-field",
            "text:modification-date",
            "text:modification-time",
            "text:note",
            "text:note-ref",
            "text:object-count",
            "text:page-continuation",
            "text:page-count",
            "text:page-number",
            "text:page-variable-get",
            "text:page-variable-set",
            "text:paragraph-count",
            "text:placeholder",
            "text:print-date",
            "text:printed-by",
            "text:print-time",
            "text:reference-mark",
            "text:reference-mark-end",
            "text:reference-mark-start",
            "text:reference-ref",
            "text:ruby",
            "text:s",
            "text:script",
            "text:sender-city",
            "text:sender-company",
            "text:sender-country",
            "text:sender-email",
            "text:sender-fax",
            "text:sender-firstname",
            "text:sender-initials",
            "text:sender-lastname",
            "text:sender-phone-private",
            "text:sender-phone-work",
            "text:sender-position",
            "text:sender-postal-code",
            "text:sender-state-or-province",
            "text:sender-street",
            "text:sender-title",
            "text:sequence",
            "text:sequence-ref",
            "text:sheet-name",
            "text:soft-page-break",
            "text:span",
            "text:subject",
            "text:tab",
            "text:table-count",
            "text:table-formula",
            "text:template-name",
            "text:text-input",
            "text:time",
            "text:title",
            "text:toc-mark",
            "text:toc-mark-end",
            "text:toc-mark-start",
            "text:user-defined",
            "text:user-field-get",
            "text:user-field-input",
            "text:user-index-mark",
            "text:user-index-mark-end",
            "text:user-index-mark-start",
            "text:variable-get",
            "text:variable-input",
            "text:variable-set",
            "text:word-count",
        },
    },
    "text:span": {
        "allowed_attributes": {"text:class-names", "text:style-name"},
        "allowed_children": {
            str,
            "dr3d:scene",
            "draw:a",
            "draw:caption",
            "draw:circle",
            "draw:connector",
            "draw:control",
            "draw:custom-shape",
            "draw:ellipse",
            "draw:frame",
            "draw:g",
            "draw:line",
            "draw:measure",
            "draw:page-thumbnail",
            "draw:path",
            "draw:polygon",
            "draw:polyline",
            "draw:rect",
            "draw:regular-polygon",
            "office:annotation",
            "office:annotation-end",
            "presentation:date-time",
            "presentation:footer",
            "presentation:header",
            "text:a",
            "text:alphabetical-index-mark",
            "text:alphabetical-index-mark-end",
            "text:alphabetical-index-mark-start",
            "text:author-initials",
            "text:author-name",
            "text:bibliography-mark",
            "text:bookmark",
            "text:bookmark-end",
            "text:bookmark-ref",
            "text:bookmark-start",
            "text:change",
            "text:change-end",
            "text:change-start",
            "text:chapter",
            "text:character-count",
            "text:conditional-text",
            "text:creation-date",
            "text:creation-time",
            "text:creator",
            "text:database-display",
            "text:database-name",
            "text:database-next",
            "text:database-row-number",
            "text:database-row-select",
            "text:date",
            "text:dde-connection",
            "text:description",
            "text:editing-cycles",
            "text:editing-duration",
            "text:execute-macro",
            "text:expression",
            "text:file-name",
            "text:hidden-paragraph",
            "text:hidden-text",
            "text:image-count",
            "text:initial-creator",
            "text:keywords",
            "text:line-break",
            "text:measure",
            "text:meta",
            "text:meta-field",
            "text:modification-date",
            "text:modification-time",
            "text:note",
            "text:note-ref",
            "text:object-count",
            "text:page-continuation",
            "text:page-count",
            "text:page-number",
            "text:page-variable-get",
            "text:page-variable-set",
            "text:paragraph-count",
            "text:placeholder",
            "text:print-date",
            "text:printed-by",
            "text:print-time",
            "text:reference-mark",
            "text:reference-mark-end",
            "text:reference-mark-start",
            "text:reference-ref",
            "text:ruby",
            "text:s",
            "text:script",
            "text:sender-city",
            "text:sender-company",
            "text:sender-country",
            "text:sender-email",
            "text:sender-fax",
            "text:sender-firstname",
            "text:sender-initials",
            "text:sender-lastname",
            "text:sender-phone-private",
            "text:sender-phone-work",
            "text:sender-position",
            "text:sender-postal-code",
            "text:sender-state-or-province",
            "text:sender-street",
            "text:sender-title",
            "text:sequence",
            "text:sequence-ref",
            "text:sheet-name",
            "text:soft-page-break",
            "text:span",
            "text:subject",
            "text:tab",
            "text:table-count",
            "text:table-formula",
            "text:template-name",
            "text:text-input",
            "text:time",
            "text:title",
            "text:toc-mark",
            "text:toc-mark-end",
            "text:toc-mark-start",
            "text:user-defined",
            "text:user-field-get",
            "text:user-field-input",
            "text:user-index-mark",
            "text:user-index-mark-end",
            "text:user-index-mark-start",
            "text:variable-get",
            "text:variable-input",
            "text:variable-set",
            "text:word-count",
        },
    },
}

MAP = MappingProxyType(EM)
