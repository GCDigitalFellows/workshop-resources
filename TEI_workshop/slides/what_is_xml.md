[<<<Previous  ](what_is_tei.md) | [Next>>>](modules.md)

# What is XML? 

XML, or *eXtensible Markup Language*, is not actually a language, but a framework for creating more specific markup languages.

TEI evolved from XML, made specifically to render humanities textual data. It carries with it many aspects and qualities that are inherent to XML. Let's look at some of these qualities that TEI inherits. 

First, "eXtensible" means that you can extend, or customize, the XML. In other words, XML allows you to create your own tags.

Second, the documents must be *well-formed* according to a defined syntax---tags must nest properly, that is, you must always close the last tag you opened before closing a tag you opened previous to the last one.

    <sentence>This is <emphasis>bad</sentence>form.</emphasis> 

    <sentence>This is <emphasis>good</emphasis>form.</sentence>

Finally, XML is intersested in the meaning of data in addition to its presentation. Contrast this to HTML, which concerns itself with how elements are laid out on the screen.

## XML declaration

Every TEI document begins with an XML declaration, which specifies the *type* of document as well as how a computer might *process* that document, validating it against your chosen schema, in this case, a TEI schema. 

This declaration is formally known as the *DTD*, or *Document Type Definition*. For the purposes of this workshop, you don't need to know exactly what this complicated code says, but you do need to know that it's necessary for the computer to read the TEI. The DTD establishes and specifies the relationship between TEI and its parent language, XML. You might think of it as a dictionary that the computer uses to read and understand the TEI elements in the document.

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
    <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
        schematypens="http://purl.oclc.org/dsdl/schematron"?>

[<<<Previous  ](what_is_tei.md)| [Next>>>](modules.md)