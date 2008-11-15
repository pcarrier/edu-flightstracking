<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
				xmlns:f="http://snibbits.net/~gcarrier/ns/tracking"
                version="1.0"
                >
 
    <xsl:output method="xml" indent="yes"/>

	<xsl:template match="/">
		<xsl:message>Template flighttraking</xsl:message>
    	<xsl:element name="kml">
    		<xsl:element name="Document">
    			<xsl:element name="name">
    				<xsl:text>Actualité des vols</xsl:text>
    			</xsl:element>
    			<xsl:element name="description">
    				<xsl:text>Une carte des vols - cliquer sur un symbole pour voir les vols à l'arrivé en provenance de Paris, Orly</xsl:text>
    			</xsl:element>
    		
    			<xsl:apply-templates select="//f:locations"/>
    		</xsl:element>
    	</xsl:element>
    </xsl:template>
    
    
	<xsl:template match="f:locations">
	<xsl:for-each select="//f:location">
    		<xsl:element name="Placemark">
    				<xsl:element name="name"><xsl:value-of select="@name"/></xsl:element>
    				<xsl:element name="description"><![CDATA[ DES TRUCS]]> </xsl:element>
    				<xsl:element name="Point">
    				<xsl:element name="coordinates">
    					<xsl:value-of select="//f:coordinates"/>
    				</xsl:element>
    			</xsl:element>
    		</xsl:element>
    	</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>